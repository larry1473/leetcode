/**
 * @author Larry Fotso Guiffo.
 * This code solves the leet code proble roman to integer.
 * time taken by the code to solve the problem:6ms
 * the space used to solve this problem is:44 MB.
 * Date: 2023-07-13 
 */

public class RomanToInt {

    public static int O_F(String s){
        if(s.equals("I")){
            return 1;
        }
        else if(s.equals("V")){
            return 5;
        }
        else if(s.equals("X")){
            return 10;
        }
        else if(s.equals("L")){
            return 50;
        }
        else if(s.equals("C")){
            return 100;
        }
        else if(s.equals("D")){
            return 500;
        }
        else if(s.equals("M")){
            return 1000;
        }
       return 0;
    }
    public static int romanToInt(String s) {
        int res = 0;
        if(s.length() == 1){
            String tes = ""+s; 
            return O_F(tes);
        }
        else{
            int count = s.length()-1;
            int prevNum = 0;
            while (count >= 0){
                String tes = ""+ s.charAt(count);
                int currentNum = O_F(tes);
                if( currentNum < prevNum && prevNum != 0){
                    res -= currentNum;
                  
                }
                else{
                    res += currentNum;
                  
                }
                prevNum = currentNum;
                count--;
              
            }
            return res;
        }


    
}
    
}
