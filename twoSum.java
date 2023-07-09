
/**
 * @author Larry Fotso Guiffo.
 * This code solves the leet code proble twoSum
 * time taken by the code to solve the problem:85ms
 * Date: 2023-07-9
 */
class twoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] lis  = new int[2];
        int res = target;
        int front = 0;
        int end = nums.length - 1;

        while(end >= front){
            if(end == nums.length - 1){
                res -= nums[front]; 
            }
            if(res == nums[end] && (end != front)){
                break;
            }
            if(end == front){
                end = nums.length - 1;
                res = target;
                front++;
            }
            else{
                end--;
            }
        }
        lis[0] = front;
        lis[1] = end;
        return lis;
        
    }
}