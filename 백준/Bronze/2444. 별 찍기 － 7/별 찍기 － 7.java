import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuffer blank = new StringBuffer();
        StringBuilder star = new StringBuilder();

        for(int i=0;i<t;i++){
            blank.append(" ");
        }

        for(int i=1;i<=t;i++){
            if(star.length() == 0){
                star.append("*");
            }
            
            else{
                star.append("**");
            }
            if(blank.length() > 0){
                blank.delete(0,1);
            }
            System.out.println(blank.toString() + star);
            
        }

        for(int i=0;i<t-1;i++){
            star.delete(0, 2);
            blank.append(" ");
            System.out.println(blank.toString() + star);
        }

    }

}