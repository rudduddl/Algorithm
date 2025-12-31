import java.util.Scanner;
import java.util.Collections;
import java.util.*;

public class Main {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        if (sc.hasNextInt()) {

            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();

            if(a == b && b == c){
                System.out.println(10000 + a * 1000);
            }
            else if(a == b || a == c){
                System.out.println(1000 + a * 100);
            }    
            else if(b == c){
                System.out.println(1000 + b * 100);
            }
            else {
                int[] data = {a, b, c};
                int max = Integer.MIN_VALUE;

                for (int i=0; i < data.length; i++){
                    if(data[i] > max){
                        max = data[i];
                    }
                }

                System.out.println(max * 100);
            }
        }

    }
}