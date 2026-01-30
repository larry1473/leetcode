
import java.util.*;
public class Reverse{

    public static String reverseWords (String str){
        String[] arr = str.trim().split("\\s+");
        Collections.reverse(Arrays.asList(arr));
        return String.join(" ", arr);
    }
}