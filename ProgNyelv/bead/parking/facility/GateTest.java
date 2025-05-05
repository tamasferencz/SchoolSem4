package parking.facility;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import parking.ParkingLot;
import vehicle.Car;
import vehicle.Size;

import static org.junit.jupiter.api.Assertions.*;

import java.lang.reflect.Method;

public class GateTest {

    private ParkingLot lot;
    private Gate gate;

    @BeforeEach
    public void setUp() {
        lot = new ParkingLot(3, 5);
        gate = new Gate(lot);
    }

    @Test
    public void testFindAnyAvailableSpaceForCar() {
        Car smallCar = new Car("ABC123", Size.SMALL, 0);
        Car largeCar = new Car("BIG999", Size.LARGE, 1);

        assertNotNull(gate.findAnyAvailableSpaceForCar(smallCar));
        assertNotNull(gate.findAnyAvailableSpaceForCar(largeCar));

        gate.registerCar(new Car("PRE999", Size.LARGE, 0));
        assertNotNull(gate.findAnyAvailableSpaceForCar(smallCar));
    }

    @ParameterizedTest
    @CsvSource({
            "SML001, SMALL, 0",
            "BIG001, LARGE, 1"
    })
    public void testFindPreferredAvailableSpaceForCar(String plate, Size size, int preferredFloor) {
        Car car = new Car(plate, size, preferredFloor);
        assertNotNull(gate.findPreferredAvailableSpaceForCar(car));
    }

    @ParameterizedTest
    @CsvSource({
            "SML002, SMALL, 0",
            "BIG002, LARGE, 2"
    })
    public void testRegisterCar(String plate, Size size, int preferredFloor) {
        Car car = new Car(plate, size, preferredFloor);
        assertTrue(gate.registerCar(car));
        assertTrue(lot.toString().contains("S") || lot.toString().contains("L"));
    }

    @ParameterizedTest
    @CsvSource({
            "SML003, SMALL, 0",
            "BIG003, LARGE, 2"
    })
    public void testDeRegisterCar(String plate, Size size, int preferredFloor)
            throws NoSuchMethodException, IllegalAccessException, java.lang.reflect.InvocationTargetException {
        Car car = new Car(plate, size, preferredFloor);
        assertTrue(gate.registerCar(car));

        String ticketId = car.getTicketId();
        assertNotNull(ticketId);

        gate.deRegisterCar(ticketId);

        Method method = gate.getClass().getDeclaredMethod("findTakenSpaceByCar", Car.class);
        method.setAccessible(true);

        assertNull(method.invoke(gate, car));
    }
}
