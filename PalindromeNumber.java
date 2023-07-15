import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leet code problem palindrome number. 
 * Memory usage:43.5 MB.
 * time taken by the code to solve the problem: 615 ms.
 * Date: 2023-07-9.
 */
public class PalindromeNumber {
    public boolean isPalindrome(int x) {
         if(x < 0 ){
          return false;
       }
       else{
          Stack<Integer> stack = new Stack<>();
          Queue<Integer> queue = new LinkedList<>();
          int num = x;
          int number = 0;
          
           while (num > 0){
            number = num % 10;
            num /= 10;
            stack.push(number);
            queue.add(number);
            
        }
        
        while(true){
           System.out.println(stack);
           System.out.println(queue);
              
            if(stack.size() == 0 || queue.size() == 0){
                return true;
            }
            else if(stack.peek() == queue.peek()){
                stack.pop();
                queue.remove();
            }
            else if(stack.peek() != queue.peek()){
                break;
            }
        }
        return false;

       }
        
    }
}
    

