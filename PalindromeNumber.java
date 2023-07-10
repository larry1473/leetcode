import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

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
    

