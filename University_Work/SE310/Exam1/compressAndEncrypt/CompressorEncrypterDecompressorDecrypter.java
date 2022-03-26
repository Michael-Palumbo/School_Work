package compressAndEncryptExamVersion;

import javax.crypto.*;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.zip.DeflaterOutputStream;
import java.util.zip.InflaterOutputStream;

/**
 * @author Sean Grimes, sean@seanpgrimes.com
 *
 * This class allows you to compress & encrypt (in that order) and decrypt & decompress
 * (in that order). It works on a raw byte[] only, though could be extended for other
 * types of data. This should not, seriously, ever be used in a real application. It's
 * not remotely secure, it doesn't operate on streams, it has a terribly simple
 * interface which makes questionable choices for ease of understanding to help with
 * it's purpose - a class exam. Also, please don't take checked exceptions and convert
 * them to unchecked exceptions in a real program.
 *
 * Data is compressed first, then encrypted. Encrypted data should appear random, and
 * random data doesn't get compressed very well. Data must then first be decrypted
 * before it can be decompressed. How effectively the data is compressed will entirely
 * depend on the input data. Random data won't be very compressed, an array of all 0s
 * will be compressed with great effect.
 *
 * NOTE: The same type of encryption algorithm used for encryption needs to be used for
 * decryption. If you pass true to compressAndEncryptBytes for the encryptionFlag you
 * must also pass true to decompressAndDecryptBytes for the decryptionFlag
 *
 * NOTE: Similar to above, the same type of compression algorithm used for compression
 * needs to be used for decompression. If you pass true to compressAndEncryptBytes for
 * the compressorFlag you *must* also pass true to decompressAndDecryptBytes for the
 * decompressorFlag
 *
 * This class is not thread safe in any way.
 */
public class CompressorEncrypterDecompressorDecrypter {
    private SecretKey sKey;
    /**
     * Takes an array of bytes, compressed them, then encrypts them. Compressing the
     * bytes post encryption results in little to no benefit as the compressed data
     * should appear to be largely random, and random data cannot be effectively
     * compressed. This function allows for AES and DES encryption, set based on
     * encryptionFlag, where true give AES and false gives DES
     * NOTE: Compressed size will vary wildly based on input data. Random data will
     * offer (possibly) no size reduction or a slight size increase. An array of all
     * zeros will be compressed with very high efficiency.
     * @param bytes The bytes to be compressed and encrypted
     * @param encryptionFlag When this is true the AES algorithm is used, when this is
     *                       false the much weaker DES encryption algorithm is used
     * @param compressorFlag When this is true a good compression algorithm will be
     *                       used, when this is false a bad compression algorithm will
     *                       be used
     * @return The compressed and encrypted bytes
     */
    public byte[] compressAndEncryptBytes(byte[] bytes, EncryptType encryptionType,
                                          CompType compressorType) {
        
        Cipher cipher;
        KeyGenerator keyGen;
        SecureRandom sRand;
        String cipherType;
        String keyType;

        byte[] compressedAndEncryptedBytes;
        
        // Where the compressed bytes will be stored prior to encryption
        byte[] compressedBytes;
        // Use the good compression algorithm
        switch(encryptionType){
            case EncryptType.AES: {
                cipherType = "AES";
                keyType = "AES";
                
                // First compress the bytes
                ByteArrayOutputStream baos = new ByteArrayOutputStream();
                DeflaterOutputStream dos = new DeflaterOutputStream(baos);
                try {
                    dos.write(bytes);
                    dos.flush();
                    dos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                // Get the compressed bytes from the output stream, ready for encryption
                compressedBytes = baos.toByteArray();
                break;
            }
            //Use the bad Compression algorithm
            case EncryptType.DES: {
                cipherType = "DES";
                keyType = "DES";
                
                // Use the bad compression algorithm
                compressedBytes = new byte[bytes.length];
                for (int i = 0; i < bytes.length; ++i) {
                    byte bite = (byte) (bytes[i] >> 0);
                    compressedBytes[i] = bite;
                }
                break;
            }
            default : {
                throw new RuntimeException("Unknown type of Encryption");
                return false;
            }
        }

        // The ciper is, essentially, the encryption algorithm being used. You could spend a
        // full degree on understanding the details here but it's not important for this
        // question, just think of it as the type of encryption algorithm being used.
        // The cipher type and the key generator type based on encryption algorithm
        // being used (the encryptionType variable)
       
        try{
            // Initialize the cipher
            cipher = Cipher.getInstance(cipherType);
            // The key generator that will be used to generate the key (PW)
            keyGen = KeyGenerator.getInstance(keyType);
        }
        catch(NoSuchAlgorithmException | NoSuchPaddingException e){
            throw new RuntimeException("Checked to unchecked encrypter");
        }

        // Better, but slower than Random()
        sRand = new SecureRandom();
        // Need to initialize the key generator with the random number generator
        keyGen.init(sRand);
        // The key that will be used by the algorithm, it's a class variable because it
        // needs to be used in the decryption algorithm
        this.sKey = keyGen.generateKey();

        try{
            // Init the cipher to encrypt the byte array
            cipher.init(Cipher.ENCRYPT_MODE, this.sKey);
            // Encrypt the data
            compressedAndEncryptedBytes = cipher.doFinal(compressedBytes);
        }
        catch(InvalidKeyException | IllegalBlockSizeException | BadPaddingException e){
            throw new RuntimeException("Checked to unchecked encrypting");
        }

        return compressedAndEncryptedBytes;
    }

    /**
     * Takes an array of compressed and encrypted bytes and decompresses & decrypts
     * these bytes
     * @param bytes The bytes to be decompressed and decrypted
     * @param decryptionFlag When this is true the AES algorithm is used, when this is
     *                       false the much weaker DES algorithm is used. Please
     *                       remember that you need to use the same algorithm here that
     *                       you used for encryption!!!
     * @param decompressionFlag When this is true the good algorithm is used, when this
     *                         is false the bad algorithm is used. Please remember that
     *                         you need to use the same algorithm here that you used
     *                          for compression!!!
     * @return The decompressed and decrypted bytes
     */
    public byte[] decompressAndDecryptBytes(byte[] bytes, DecryptType decryptionType,
                                            DecryptType decompressionType) {
        // Decrypt the bytes first, then decompress
        byte[] decryptedBytes;

        Cipher cipher;
        KeyGenerator keyGen;
        SecureRandom sRand;
        SecretKey sKey;
        String cipherType;
        String keyType;


        switch(decryptionType) {
            case DecryptType.AES: {
                // Using AES
                cipherType = "AES";
                keyType = "AES";
            }
            case DecryptType.DES: {
                // Using DES
                cipherType = "DES";
                keyType = "DES";
            }
        }

        try{
            cipher = Cipher.getInstance(cipherType);
            keyGen = KeyGenerator.getInstance(keyType);
        }
        catch(NoSuchAlgorithmException | NoSuchPaddingException e){
            throw new RuntimeException("Checked to unchecked decrypter");
        }

        try {
            cipher.init(Cipher.DECRYPT_MODE, this.sKey);
            decryptedBytes = cipher.doFinal(bytes);
        }
        catch(InvalidKeyException | IllegalBlockSizeException | BadPaddingException e) {
            throw new RuntimeException("Checked to unchecked decrypting");
        }

        byte[] decompressedBytes;
        // Use the good decompression algorithm
        switch(decryptionType) {
            case DecryptType.AES: {
                // Decompress the decrypted bytes
                ByteArrayOutputStream baos = new ByteArrayOutputStream();
                InflaterOutputStream ios = new InflaterOutputStream(baos);
                try {
                    ios.write(decryptedBytes);
                    ios.flush();
                    ios.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }

                decompressedBytes = baos.toByteArray();
            }
        // Use the bad decompression algorithm
            case DecryptType.AES: {
                decompressedBytes = new byte[decryptedBytes.length];
                for (int i = 0; i < decompressedBytes.length; ++i) {
                    byte bite = (byte) (decryptedBytes[i] << 0);
                    decompressedBytes[i] = bite;
                }
            }
        }

        return decompressedBytes;
    }

    // Here is an example usage of the class
    public static void main(String[] args) {
        final EncryptType AES = EncryptType.AES;
        final EncryptType DES = EncryptType.DES;
        final DecryptType GOOD_COMP = DecryptType.GOOD_COMP;
        final DecryptType BAD_COMP = DecryptType.BAD_COMP;
        final int LENGTH = 15;

        CompressorEncrypterDecompressorDecrypter cedd =
                new CompressorEncrypterDecompressorDecrypter();
        byte[] inputNumbers = new byte[LENGTH];
        for(int i = 0; i < LENGTH; ++i) inputNumbers[i] = (byte) i;

        // Print the original data
        for(byte b : inputNumbers) System.out.println("Original: " + b);

        // Compress and encrypt the array of numbers
        byte[] comEnc = cedd.compressAndEncryptBytes(inputNumbers, AES, GOOD_COMP);
        System.out.println("-----");
        // Print the encrypted / compressed bytes (notice no effective compression due
        // to the input data)
        for(byte b : comEnc) System.out.println("comEnd: " + b);

        // decompress and decrypt the data
        byte[] decDec = cedd.decompressAndDecryptBytes(comEnc, AES, GOOD_COMP);
        System.out.println("-----");
        // Print the decompressed and decrypted data
        for(byte b : decDec) System.out.println("decDec: " + b);

        // Go through and prove the original array data is equal to the returned array
        // of data
        if(decDec.length != inputNumbers.length)
            System.out.println("Lengths are not the same");
        boolean problem = false;
        for(int i = 0; i < inputNumbers.length; ++i) {
            if (inputNumbers[i] != decDec[i])
                problem = true;
        }

        if(problem) System.out.println("Input and returned data are not the same");
        else System.out.println("Input and returned data are the same");

    }
}
