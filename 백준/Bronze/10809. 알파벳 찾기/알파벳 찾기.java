import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map.Entry;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String sentence = br.readLine();
        char[] words = sentence.toCharArray();
        HashMap<Character, Integer> alphabets = new HashMap<>();
        for(int i=0;i<26;i++){
            alphabets.put((char)('a' + i), -1);
        }
        
        for(int i=0;i<words.length;i++){
            if(alphabets.get(words[i]) == -1){
                alphabets.put(words[i], i);
            }
        }

        for(Entry<Character, Integer> entrySet : alphabets.entrySet()){
            System.out.print(entrySet.getValue() + " ");
        }

    }
}