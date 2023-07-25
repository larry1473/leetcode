import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

/**
 * @author Larry Fotso Guiffo.
 * This code solves the leetcode problem is valid . 
 * Memory usage:44.15 MB.
 * time taken by the code to solve the problem: 70ms.
 * Date: 2023-07-9.
 */

public class IsValid {

    public boolean isValid(String s) {
        String[] opens  = {"(", "{", "["};
        ArrayList<String> opens1 = new ArrayList<>(Arrays.asList(opens));;
        String[] closes = {")","}","]"};
        List closes1 = Arrays.asList(closes);
        Stack<String> stack = new Stack<>();
        int count = 0;
        while (count < s.length()){
           if(stack.size() != 0 ){
               if(opens1.contains(stack.peek())){
                   if(closes1.indexOf(""+s.charAt(count)) == opens1.indexOf(stack.peek())){
                       stack.pop();
                   }
                   else{
                       stack.push(""+s.charAt(count));
                   }
               }
               else{
                   stack.push(""+s.charAt(count));
               }
           }
           else{
                   stack.push(""+s.charAt(count));
            }
           
           count++;
        }
        return stack.size() == 0;
        
    }
}
