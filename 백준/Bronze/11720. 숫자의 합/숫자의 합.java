import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int numberLength = Integer.parseInt(br.readLine());
        String numbers = br.readLine();

        int result = 0;

        for(int i=0;i<numberLength;i++){
            result += (numbers.charAt(i) - '0');
        }

        System.out.print(result);

    }
}