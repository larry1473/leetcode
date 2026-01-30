import java.util.*;
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leetcode problem twoSum
 * time taken by the code to solve the problem:85ms
 * Date: 2023-07-9
 */
class TwoSum {
    public static int[] twoSum(int[] nums, int target){
        HashMap<Integer,Integer>dico = new HashMap<>(); 
       for( int i= 0; i < nums.length; i++){
        if(dico.containsKey(nums[i])){
                return new int[] {dico.get(nums[i]), i};
            }
            else{
                dico.put(target-nums[i],i);
            }
       }
       return new int[]{-1,-1};


    }
}