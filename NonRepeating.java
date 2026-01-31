import java.util.*;
public class NonRepeating {

    public static int firstUnique(String s){
        HashMap<Character,Integer> dico = new HashMap<>();
        for (char c : s.toCharArray()){
            if (dico.containsKey(c)){
                dico.put(c,dico.get(c)+1);

            }
            else{
                dico.put(c,1);
            }
        }
        for(int i=0; i<s.length();i++){
            if(dico.get(s.charAt(i)) == 1){
                return i;
            }
        }
        return -1;

    }
    
}
