public class Point {

    public double x = 0.0;
    public double y = 0.0;

    public void move(double dx, double dy) {
        this.x += dx;
        this.y += dy;
    }

    public void mirror(double cx, double cy) {
        x = 2 * cx - x;
        y = 2 * cy - y;
    }

    public void printPoint() {
        System.out.println("P(" + this.x + ", " + this.y + ")");
    }

}
