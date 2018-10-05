package org.rgbit.rgpg;

/**
 * Generate the password with the necessary information and the specified input.
 */
public class Generate {
  private static StringTrans trans = StringTrans.maketrans(Essential.TRANS_IN, Essential.TRANS_OUT);

  /**
   * Generate a password of the specified length based on the input.
   * @param input Specified input string.
   * @param length The length of the password to be generated. Invalid part longer than 32.
   * @return Generated password.
   */
  public static String generate(String input, int length) {
    String md5K1 = MD5Helper.md5(Essential.K1 + input);
    String md5K2 = MD5Helper.md5(Essential.K2 + md5K1);
    String md5K3 = MD5Helper.md5(Essential.K3 + md5K1);

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < md5K1.length(); ++i) {
      if (md5K2.charAt(i) < md5K3.charAt(i)) {
        sb.append(md5K3.charAt(i));  // Make the letter(a-f) more
      } else {
        sb.append(md5K2.charAt(i));
      }
    }

    return Essential.FIRST + trans.translate(sb.substring(1, Math.min(length, sb.length())));
  }

  /**
   * Generate a password with a fixed length of 16.
   * @param input Specified input string.
   * @return Generated password.
   */
  public static String generate(String input) {
    return generate(input, 16);
  }
}
