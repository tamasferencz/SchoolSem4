package text.to.numbers;

import static check.CheckThat.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.condition.*;
import org.junit.jupiter.api.extension.*;
import org.junit.jupiter.params.*;
import org.junit.jupiter.params.provider.*;
import check.*;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;


public class SingleLineFileTest {
    private static final String TEST_FILE = "testfile.txt";

    private void createTestFile(String content) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(TEST_FILE))) {
            writer.write(content);
        }
    }

    @ParameterizedTest
    @CsvSource(textBlock = """
        '1 2 3', 6
        '10 20 30', 60
        '100 -50 25', 75
        '5 -5', 0
        '0', 0
        'abc 10 def 20', 30
        '', 0
    """)
    public void testAddNumbers(String content, int expectedSum) throws IOException {
        createTestFile(content);
        assertEquals(expectedSum, SingleLineFile.addNumbers(TEST_FILE));
    }
}
