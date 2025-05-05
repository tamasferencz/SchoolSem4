package parking;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import parking.ParkingLot;
import parking.facility.Space;
import vehicle.Car;
import vehicle.Size;

import static org.junit.jupiter.api.Assertions.*;

public class ParkingLotTest {

    @Test
    public void testConstructorWithInvalidValues() {
        assertThrows(IllegalArgumentException.class, () -> new ParkingLot(0, 5));
        assertThrows(IllegalArgumentException.class, () -> new ParkingLot(-1, 5));

        assertThrows(IllegalArgumentException.class, () -> new ParkingLot(3, 0));
        assertThrows(IllegalArgumentException.class, () -> new ParkingLot(3, -1));
    }

    @Test
    public void testTextualRepresentation() {
        ParkingLot parkingLot = new ParkingLot(2, 3);

        Space space1 = parkingLot.getFloorPlan()[0][0];
        space1.addOccupyingCar(new Car("ABC123", Size.SMALL, 1));

        Space space2 = parkingLot.getFloorPlan()[1][1];
        space2.addOccupyingCar(new Car("XYZ789", Size.LARGE, 1));

        String expected = "S X X \n" +
                "X L X \n";

        assertEquals(expected, parkingLot.toString());
    }
}
