import java.util.HashMap;
public class FirstRepeating {


    public static char FirstRepeatingChar(String s){
        HashMap<Character,Integer> counts = new HashMap<>();
        for (int i = 0; i < s.length(); i++ ){
            if(counts.containsKey(s.charAt(i))){
                counts.put(s.charAt(i),counts.get(s.charAt(i))+ 1);
            }
            else{
                counts.put(s.charAt(i),1);
            }
            
        }
        for (int i = 0;i < s.length(); i++){
            if(counts.get(s.charAt(i)) == 1){
                return s.charAt(i);
            }
        }
        return '_'; 
    }
}
