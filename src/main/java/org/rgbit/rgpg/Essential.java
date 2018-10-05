package org.rgbit.rgpg;

/**
 * Necessary configuration information.
 *
 * <p>Class {@link Generate Generate} Will use this information to generate a password.
 *
 * <p>{@link #K1 K1}, {@link #K2 K2} {@link #K3 K3} Used to generate MD5 digest strings.
 *
 * <p>{@link #FIRST FIRST} Specify the first character of the generated password.
 *
 * <p>{@link #TRANS_IN TRANS_IN}, {@link #TRANS_OUT TRANS_OUT} Used to perform
 * {@link StringTrans StringTrans} on the generated password.
 */
public class Essential {
  public static final String K1 = "123456";
  public static final String K2 = "";
  public static final String K3 = "";

  public static final char FIRST = 'K';

  public static final String TRANS_IN = "1234567890abcdef";
  public static final String TRANS_OUT = "abcdef1234567890";
}
