public class PointMain {
    public static void main(String[] args) {
        Point p = new Point();

        p.x = 1;
        p.y = 2;
        p.printPoint();
        p.move(2, 3);
        p.printPoint();

        p.mirror(1, 1);
        p.printPoint();

        Point2 p2 = new Point2();
        Point2 p3 = new Point2();

        p2.x = 1;
        p2.y = 1;

        p3.x = 5;
        p3.y = 5;

        System.out.print("P2 = ");
        p2.printPoint();
        System.out.print("P3 = ");
        p3.printPoint();

        p2.mirror(p3);
        System.out.print("P2 mirrored: ");
        p2.printPoint();
    }
}
