
public class main 
{
    public static void main(String[] args) throws Exception 
    {
        String plaintext = "Shoot";
        String path2Key = "../exampleOTPtxt";

        // Encoding
        String encodedText = OTP.encode(plaintext, path2Key);
        System.out.println("Encoded: " + encodedText);

        // Decoding
        String decodedText = OTP.decode(encodedText, path2Key);
        System.out.println("Decoded: " + decodedText);
    }
}