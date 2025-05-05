package parking.facility;

import vehicle.Car;
import vehicle.Size;

public class Space {

    private final int floorNumber;
    private final int spaceNumber;
    private Car occupyingCar;

    public Space(int floorNumber, int spaceNumber) {
        this.floorNumber = floorNumber;
        this.spaceNumber = spaceNumber;
        this.occupyingCar = null;
    }

    public boolean isTaken() {
        return occupyingCar != null;
    }

    public void addOccupyingCar(Car car) {
        this.occupyingCar = car;
    }

    public void removeOccupyingCar() {
        this.occupyingCar = null;
    }

    public String getCarLicensePlate() {
        return occupyingCar.getLicensePlate();
    }

    public Size getOccupyingCarSize() {
        return occupyingCar.getSpotOccupation();
    }

    public int getFloorNumber() {
        return this.floorNumber;
    }

    public int getSpaceNumber() {
        return this.spaceNumber;
    }

}
