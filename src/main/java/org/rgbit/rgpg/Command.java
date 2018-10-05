package org.rgbit.rgpg;

/**
 * Command line parameter processing.
 */
public class Command {
  private static void helpOption() {
    System.out.println("Usage: rgpg [OPTIONS]... STRING");
    System.out.println();
    System.out.println("Generate a password based on the specified character");
    System.out.println();
    System.out.println("Options:");
    System.out.println("  -l, --length  specify the length of the password.");
    System.out.println("                Valid values range from 1-32.");
    System.out.println("  -h, --help    display this help and exit.");
  }

  private static void unknownOption(String option) {
    System.out.println(String.format("rgpg: unknown option %s", option));
    System.out.println("Try 'rgpg --help' for more information.");
  }

  private static void errorOption() {
    System.out.println("Usage: rgpg [OPTIONS]... STRING");
    System.out.println("Try 'rgpg --help' for more information.");
  }

  private static void lengthOption(String input, int length) {
    System.out.println(Generate.generate(input, length));
  }

  private static void defaultOption(String input) {
    System.out.println(Generate.generate(input));
  }

  public static void main(String[] args) {
    if (args.length == 0) {
      return;
    }

    if (args[0].equals("-h") || args[0].equals("--help")) {
      helpOption();
      return;
    }

    if (args[0].startsWith("-")) {
      if (args[0].equals("-l") || args[0].equals("--length")) {
        try {
          lengthOption(args[2], Integer.valueOf(args[1]));
        } catch (IndexOutOfBoundsException | NumberFormatException e) {
          errorOption();
        }
      } else {
        unknownOption(args[0]);
      }
      return;
    }

    defaultOption(args[0]);
  }
}
