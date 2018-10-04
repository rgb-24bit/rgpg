package org.rgbit.rgpg;

public class Generate {
  private StringTrans trans = StringTrans.maketrans(Config.TRANS_IN, Config.TRANS_OUT);

  public String generate(String input, int length) {
    String md5K1 = MD5Helper.md5(Config.K1 + input);
    String md5K2 = MD5Helper.md5(Config.K2 + md5K1);
    String md5K3 = MD5Helper.md5(Config.K3 + md5K1);

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < md5K1.length(); ++i) {
      if (md5K2.charAt(i) < md5K3.charAt(i)) {
        sb.append(md5K3.charAt(i));
      } else {
        sb.append(md5K2.charAt(i));
      }
    }
    String result = trans.translate(sb.toString());

    return Config.FIRST + result.substring(1, length);
  }
}
