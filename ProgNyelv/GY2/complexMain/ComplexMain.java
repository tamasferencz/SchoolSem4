package complexMain;

import complex.Complex;

public class ComplexMain {
    public static void main(String[] args) {

        Complex c1 = new Complex();
        c1.x = 1;
        c1.y = 2;

        Complex c2 = new Complex();
        c2.x = 3;
        c2.y = 4;

        System.out.println("C1 abs: " + c1.abs());

        c1.add(c2);
        c1.printComplex();

        c1.mul(c2);
        c1.printComplex();

        c1.sub(c2);
        c1.printComplex();

        c1.conjugate();
        c1.reciprocate();
    }
}
