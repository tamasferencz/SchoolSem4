package complex;

public class Complex {

    public double x = 0.0;
    public double y = 0.0;

    public void printComplex() {
        System.out.println("C = " + this.x + " + " + this.y + "i");
    }

    public double abs() {
        return ((this.x * this.x) + (this.y + this.y));
    }

    public void add(Complex a) {
        this.x += a.x;
        this.y += a.y;
    }

    public void sub(Complex a) {
        this.x -= a.x;
        this.y -= a.y;
    }

    public void mul(Complex a) {
        this.x *= a.x;
        this.y *= a.y;
    }

    public void conjugate() {
        System.out.println("Conjugalt: " + this.x + " " + (-1) * this.y + "i");
    }

    public void reciprocate() {
        double realPart = this.x / (Math.pow(this.x, 2) + Math.pow(this.y, 2));
        double imaginaryPart = this.y / (Math.pow(this.x, 2) + Math.pow(this.y, 2));

        System.out.println("Reciprok: 1 / (" + this.x + " + " + this.x + ") * 1/i = "
                + realPart + " - " + imaginaryPart + "i");
    }
}
