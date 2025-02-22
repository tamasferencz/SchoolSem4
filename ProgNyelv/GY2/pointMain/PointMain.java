package pointMain;

import point.Point;
import point.Point2;

public class PointMain {
    public static void main(String[] args) {
        Point p = new Point();

        p.setX(1);
        p.setY(2);
        p.printPoint();
        p.move(2, 3);
        p.printPoint();

        p.mirror(1, 1);
        p.printPoint();

        Point2 p2 = new Point2();
        Point2 p3 = new Point2();

        p2.setX(1);
        p2.setY(1);

        p3.setX(5);
        p3.setY(5);

        System.out.print("P2 = ");
        p2.printPoint();
        System.out.print("P3 = ");
        p3.printPoint();

        p2.mirror(p3);
        System.out.print("P2 mirrored: ");
        p2.printPoint();
    }
}
