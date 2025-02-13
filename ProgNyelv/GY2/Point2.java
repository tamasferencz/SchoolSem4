public class Point2 {

    public double x = 0.0;
    public double y = 0.0;

    public void move(double dx, double dy) {
        this.x += dx;
        this.y += dy;
    }

    public void mirror(Point2 p) {
        x = 2 * p.x - x;
        y = 2 * p.y - y;
    }

    public void printPoint() {
        System.out.println("P(" + this.x + ", " + this.y + ")");
    }
}
