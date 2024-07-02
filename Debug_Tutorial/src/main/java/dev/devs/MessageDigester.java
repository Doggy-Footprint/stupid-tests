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
        boolean updated = false;
        this.updateInternal(input);
        updated = true;
    }

    private void updateInternal(String input) {
        this.mdInstance.update(input.getBytes());
        this.digestDone = false;
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
