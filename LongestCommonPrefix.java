/**
 * @author Larry Fotso Guiffo.
 * This code solves the leet code problem palindrome number. 
 * Memory usage:40 MB.
 * time taken by the code to solve the problem: 1ms.
 * Date: 2023-07-9.
 */

public class LongestCommonPrefix {

    public  String longestCommonPrefix(String[] strs){
        String res = strs[0];
        for(int i = 1; i < strs.length; i++){
           int count = 0;
           
           if(res.length() > strs[i].length()){
              res = res.substring(0,strs[i].length());
           }
           while (count < strs[i].length()){
              if(count < res.length()){
                   if(res.charAt(count) != strs[i].charAt(count)){
                      res = res.substring(0,count);
                      
                     
                  }
              }
            
              count++;
  
        }
         
        
     }
        
     return res;
  
   
     
     }
    
}
