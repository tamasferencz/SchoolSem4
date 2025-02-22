package point;

public class Point2 {

    public double x;
    public double y;

    public double getX() {
        return this.x;
    }

    public double getY() {
        return this.y;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

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
