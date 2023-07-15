/**
 * @author Larry Fotso Guiffo.
 * This code solves the leet code problem merge two list . 
 * Memory usage:41.76 MB.
 * time taken by the code to solve the problem: 0 ms.
 * Date: 2023-07-15.
 */
public class MergeTwoList {

    

     
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
       
        ListNode res =  new ListNode(); // the list we will return 
        ListNode tail = res; 

        
        while (list1 != null && list2 != null){
            if(list1.val < list2.val){
                tail.next = list1;
                list1 = list1.next;
            }
            else{
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;

        }
        if(list1 != null){
            tail.next = list1;
        }
        else if(list2 != null){
            tail.next = list2;

        }
        return res.next;  
}
    
}
