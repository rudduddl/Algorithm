import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        boolean[] alphabets;
        String sentence;
        
        int count = 0;

        for(int i=0;i<t;i++){
            alphabets = new boolean[26];
            sentence = br.readLine();
            boolean isGroupWord = true;
            int prev = -1;


            for(int j=0;j<sentence.length();j++){
                int now = sentence.charAt(j);

                if(prev != now){
                    if(alphabets[now-'a']){
                        isGroupWord = false;
                        break;
                    }
                    alphabets[now-'a'] = true;
                }
                
                prev = now;
            }

            if(isGroupWord) count++;

        }

        System.out.print(count);

    }

}
