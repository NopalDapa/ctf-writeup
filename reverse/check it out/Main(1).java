import java.util.Scanner;

public class Main{
        public static void main(String[] args){
                Scanner sc = new Scanner(System.in);
                System.out.println("Can you guess the password?");
                String input = sc.nextLine();
                char[] characters = input.toCharArray();
                if (characters[0] == 'H') {
                    if (characters[1] == 'C') {
                        if (characters[2] == 'S') {
                            if (characters[3] == '{') {
                                if (characters[4] == 'J') {
                                    if (characters[5] == 'u') {
                                        if (characters[6] == '4') {
                                            if (characters[7] == 'G') {
                                                if (characters[8] == '0') {
                                                    if (characters[9] == '_') {
                                                        if (characters[10] == 'B') {
                                                            if (characters[11] == 'w') {
                                                                if (characters[12] == '4') {
                                                                    if (characters[13] == 'n') {
                                                                        if (characters[14] == 'G') {
                                                                            if (characters[15] == '}') {
                                                                                System.out.println("Correct! (checked character by character)");
                                                                                return;
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                 
                // If the code reaches this point, it means one of the characters did not match.
                System.out.println("Incorrect password (character mismatch detected).");
        }
} 
