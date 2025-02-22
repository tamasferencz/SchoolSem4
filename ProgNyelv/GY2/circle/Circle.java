package circle;

public class Circle {

    public double x;
    public double y;
    public double radius;

    public void setXYR(double dx, double dy, double dr) {
        this.x = dx;
        this.y = dy;
        this.radius = dr;
    }

    public void enlarge(double f) {
        this.radius *= f;
    }

    public double getArea() {
        return this.radius * this.radius * Math.PI;
    }

    public void printCircle() {
        System.out.println("Circle: (" + this.x + ", " + this.y + "), Radius = " + this.radius);
    }

}
