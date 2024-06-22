package dev.devs;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MessageDigester {
    MessageDigest mdInstance;
    boolean digestDone;

    public MessageDigester(String algorithm) throws NoSuchAlgorithmException {
        this.mdInstance = MessageDigest.getInstance(algorithm);
        this.digestDone = false;
    }

    public void update(String input) {
        this.mdInstance.update(input.getBytes());
    }

    public String digest() {
        this.digestDone = true;
        byte[] digest = mdInstance.digest();
        StringBuilder sb = new StringBuilder();
        for (byte b: digest) {
            sb.append(String.format("%02x", b & 0xff)); //type conversion signed byte -> Hexadecimal
        }
        return sb.toString();
    }
}
