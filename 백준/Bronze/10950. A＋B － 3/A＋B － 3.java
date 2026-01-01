import java.util.Scanner;

public class Main {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        if (sc.hasNextInt()) {

            int t = sc.nextInt();
            int a, b;

            for(int i=0;i<t;i++){
                a = sc.nextInt();
                b = sc.nextInt();
                System.out.println(a+b);
            }

        }

    }
}