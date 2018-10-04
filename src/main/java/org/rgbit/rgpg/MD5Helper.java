package org.rgbit.rgpg;

import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5Helper {
  public static String md5(String input, String charsetName) {
    try {
      MessageDigest md5 = MessageDigest.getInstance("MD5");
      md5.update(input.getBytes(charsetName));
      return formatDigest(md5.digest());
    } catch (NoSuchAlgorithmException | IOException e) {
      e.printStackTrace();
    }
    return null;
  }

  public static String md5(String input) {
    try {
      MessageDigest md5 = MessageDigest.getInstance("MD5");
      md5.update(input.getBytes());
      return formatDigest(md5.digest());
    } catch (NoSuchAlgorithmException e) {
      e.printStackTrace();
    }
    return null;
  }

  private static String formatDigest(byte[] bytes) {
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < bytes.length; ++i) {
      sb.append(String.format("%02X", bytes[i]));
    }

    return sb.toString();
  }
}
