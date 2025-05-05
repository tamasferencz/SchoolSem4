package parking.facility;

import java.util.ArrayList;

import parking.ParkingLot;
import vehicle.*;

public class Gate {
    private final ArrayList<Car> cars;
    private final ParkingLot parkingLot;

    public Gate(ParkingLot parkingLot) {
        this.parkingLot = parkingLot;
        this.cars = new ArrayList<>();
    }

    private Space findTakenSpaceByCar(Car c) {
        for (int i = 0; i < parkingLot.getFloorPlan().length; i++) {
            for (int j = 0; j < parkingLot.getFloorPlan()[i].length; j++) {
                Space space = parkingLot.getFloorPlan()[i][j];
                if (space.isTaken() && space.getCarLicensePlate().equals(c.getLicensePlate())) {
                    return space;
                }
            }
        }
        return null;

    }

    private Space findAvailableSpaceOnFloor(int floor, Car c) {
        Space[][] floorPlan = parkingLot.getFloorPlan();
        Space[] spaces = floorPlan[floor];

        if (c.getSpotOccupation() == Size.SMALL) {
            for (Space space : spaces) {
                if (!space.isTaken()) {
                    return space;
                }
            }
        } else if (c.getSpotOccupation() == Size.LARGE) {
            for (int i = 0; i < spaces.length - 1; i++) {
                if (!spaces[i].isTaken() && !spaces[i + 1].isTaken()) {
                    return spaces[i + 1];
                }
            }
        }

        return null;
    }

    public Space findAnyAvailableSpaceForCar(Car c) {
        Space[][] floorPlan = parkingLot.getFloorPlan();

        for (int i = 0; i < floorPlan.length; i++) {
            Space available = findAvailableSpaceOnFloor(i, c);
            if (available != null) {
                return available;
            }
        }

        return null;
    }

    public Space findPreferredAvailableSpaceForCar(Car c) {
        int preferred = c.getPreferredFloor();
        int totalFloors = parkingLot.getFloorPlan().length;

        Space preferredSpace = findAvailableSpaceOnFloor(preferred, c);
        if (preferredSpace != null) {
            return preferredSpace;
        }

        for (int offset = 1; offset < totalFloors; offset++) {
            int down = preferred - offset;
            int up = preferred + offset;

            if (down >= 0) {
                Space downSpace = findAvailableSpaceOnFloor(down, c);
                if (downSpace != null) {
                    return downSpace;
                }
            }

            if (up < totalFloors) {
                Space upSpace = findAvailableSpaceOnFloor(up, c);
                if (upSpace != null) {
                    return upSpace;
                }
            }
        }

        return null;
    }

    public boolean registerCar(Car c) {
        Space space = findPreferredAvailableSpaceForCar(c);
        if (space == null) {
            space = findAnyAvailableSpaceForCar(c);
        }

        if (space == null) {
            return false;
        }

        int floor = space.getFloorNumber();
        int index = space.getSpaceNumber();
        Space[][] floorPlan = parkingLot.getFloorPlan();

        if (c.getSpotOccupation() == Size.SMALL) {
            floorPlan[floor][index].addOccupyingCar(c);
        } else if (c.getSpotOccupation() == Size.LARGE) {
            floorPlan[floor][index - 1].addOccupyingCar(c);
            floorPlan[floor][index].addOccupyingCar(c);
        }

        c.setTicketId(c.getLicensePlate() + "_" + System.currentTimeMillis());

        cars.add(c);
        return true;
    }

    public void registerCars(Car... cars) {
        for (Car car : cars) {
            Space space = findAnyAvailableSpaceForCar(car);

            if (space == null) {
                System.err.println("Nincs szabad hely az autó számára: " + car.getLicensePlate());
                continue;
            }

            int floor = space.getFloorNumber();
            int index = space.getSpaceNumber();
            Space[][] floorPlan = parkingLot.getFloorPlan();

            if (car.getSpotOccupation() == Size.SMALL) {
                floorPlan[floor][index].addOccupyingCar(car);
            } else if (car.getSpotOccupation() == Size.LARGE) {
                floorPlan[floor][index - 1].addOccupyingCar(car);
                floorPlan[floor][index].addOccupyingCar(car);
            }

            car.setTicketId(car.getLicensePlate() + "_" + System.currentTimeMillis());
            this.cars.add(car);
        }
    }

    public void deRegisterCar(String ticketId) {
        Car carToRemove = null;

        for (Car car : cars) {
            if (ticketId.equals(car.getTicketId())) {
                carToRemove = car;
                break;
            }
        }

        if (carToRemove == null) {
            System.err.println("Nincs ilyen ticketId-hez tartozó autó: " + ticketId);
            return;
        }

        Space occupiedSpace = findTakenSpaceByCar(carToRemove);
        if (occupiedSpace == null) {
            System.err.println("Az autó nem található a parkolóban: " + ticketId);
            return;
        }

        int floor = occupiedSpace.getFloorNumber();
        int index = occupiedSpace.getSpaceNumber();
        Space[][] floorPlan = parkingLot.getFloorPlan();

        if (carToRemove.getSpotOccupation() == Size.SMALL) {
            floorPlan[floor][index].removeOccupyingCar();
        } else if (carToRemove.getSpotOccupation() == Size.LARGE) {
            floorPlan[floor][index].removeOccupyingCar();
            floorPlan[floor][index + 1].removeOccupyingCar();
        }

        cars.remove(carToRemove);
    }

}
