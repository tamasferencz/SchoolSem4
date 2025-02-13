public class CircleMain {
    public static void main(String[] args) {

        Circle c = new Circle();
        c.x = 2;
        c.y = 2;
        c.radius = 4;

        c.printCircle();

        c.enlarge(5);
        c.printCircle();
    }

}
