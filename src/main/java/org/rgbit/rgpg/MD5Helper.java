package org.rgbit.rgpg;

import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * Help complete the MD5 digest.
 */
public class MD5Helper {
  /**
   * MD5 digest on the specified string and return the hex digest string.
   * @param input The string to be MD5 digest.
   * @param charsetName Coded character set of a string.
   * @return  Hex digest string. Error returning null.
   */
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

  /**
   * MD5 digest on the specified string and return the hex digest string.
   * @param input The string to be MD5 digest.
   * @return Hex digest string.
   */
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

  /**
   * Formatted MD5 digest information as a hexadecimal string format.
   * @param bytes MD5 digest information.
   * @return Hex digest string.
   */
  private static String formatDigest(byte[] bytes) {
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < bytes.length; ++i) {
      sb.append(String.format("%02X", bytes[i]));
    }

    return sb.toString();
  }
}
