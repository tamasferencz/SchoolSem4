package text.to.numbers;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class SingleLineFile {
    public static int addNumbers(String filename) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line = reader.readLine();

            if (line == null) {
                throw new IllegalArgumentException("Empty file");
            }

            int sum = 0;
            String[] words = line.split(" ");

            for (String word : words) {
                try {
                    sum += Integer.parseInt(word);
                } catch (NumberFormatException e) {
                    System.err.println(word);
                }
            }

            return sum;
        }
    }
}
