import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int result = 0;
        String alphabets = br.readLine();
        int alphabet;
        for(int i=0;i<alphabets.length();i++){
            alphabet = alphabets.charAt(i);

            if(alphabet <= 67){ // 2
                result += 2;
            }
            else if(alphabet <= 70){ // 3
                result += 3;
            }
            else if(alphabet <= 73){ // 4
                result += 4;
            }
            else if(alphabet <= 76){ // 5
                result += 5;
            }
            else if(alphabet <= 79){ // 6
                result += 6;
            }
            else if(alphabet <= 83){ // 7
                result += 7;
            }
            else if(alphabet <= 86){ // 8
                result += 8;
            }
            else if(alphabet <= 90){ // 9
                result += 9;
            }
                
        }

        System.out.println(result + alphabets.length());
    }

        

}