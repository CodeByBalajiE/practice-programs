//missing number
class Solution {
    public int missingNumber(int[] nums) {
        int n=nums.length;
        Arrays.sort(nums);
        for(int i=0;i<=nums.length;i++){
            if(i>nums.length-1){
                return nums.length;
            }
            if(i==nums[i]){
                continue;
            }
            else
                return i;
        }
        return 0;
    }
}
