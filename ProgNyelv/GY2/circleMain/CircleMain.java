package circleMain;

import circle.Circle;

public class CircleMain {
    public static void main(String[] args) {

        Circle c = new Circle();
        c.setXYR(2, 2, 4);

        c.printCircle();

        c.enlarge(5);
        c.printCircle();
    }

}
