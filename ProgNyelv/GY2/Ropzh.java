import java.util.Scanner;

public class Ropzh {
	static Scanner scanner = new Scanner(System.in);

	public static void main(String[] args) {

		System.out.print("Give me your name: ");
		String name = scanner.nextLine();
		System.out.print("Give me your age: ");
		int age = scanner.nextInt();

		System.out.println("\nHello " + name + "! How it feels that you're " + age + " years old?");
	}
}