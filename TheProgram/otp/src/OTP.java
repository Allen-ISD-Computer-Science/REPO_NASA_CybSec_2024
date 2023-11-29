import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class OTP {

    private OTP() {
        // Private constructor to prevent multiple instantiation
    }

    private static int xor(int asciiVal, int xorAsciiVal) {
        if (asciiVal > 127) {
            throw new IllegalArgumentException("Not an ASCII value");
        }
        return asciiVal ^ xorAsciiVal;
    }

    public static String encode(String nonEncodedText, String path2Key) throws IOException{
        String key = new String(Files.readAllBytes(Paths.get(path2Key)));
        if (key.length() < nonEncodedText.length()) {
            throw new IllegalArgumentException("Key length must be greater than or equal to text length");
        }
        char[] encodedString = nonEncodedText.toCharArray();
        char[] Key = key.toCharArray();
        StringBuilder newText = new StringBuilder();
        for (int index = 0; index < encodedString.length; index++) {
            int decodedValue = ((int) encodedString[index]) ^ ((int) Key[index]);
            char decodedChar = (char) decodedValue;
            newText.append(decodedChar);
        }
        return newText.toString();
    }
    
    public static String decode(String encodedText, String path2Key) throws IOException {
        String key = new String(Files.readAllBytes(Paths.get(path2Key)));
        if (key.length() < encodedText.length()) {
            throw new IllegalArgumentException("Key length must be greater than or equal to text length");
        }
        char[] encodedString = encodedText.toCharArray();
        char[] Key = key.toCharArray();
        StringBuilder newText = new StringBuilder();
        for (int index = 0; index < encodedString.length; index++) {
            int decodedValue = ((int) encodedString[index]) ^ ((int) Key[index]);
            char decodedChar = (char) decodedValue;
            newText.append(decodedChar);
        }
        return newText.toString();
    }
    
}