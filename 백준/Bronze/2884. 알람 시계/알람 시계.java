import java.util.Scanner;

public class Main {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        if (sc.hasNextInt()) {

            int hour = sc.nextInt();
            int minutes = sc.nextInt();

            minutes -= 45;

            if (minutes < 0){
                hour -= 1;
                minutes += 60;
            }

            if (hour < 0){
                hour = 23;
            }


           
            System.out.printf("%d %d", hour, minutes);
            
        }

    }
}