import java.util.Arrays;

class miss {
    public static int missingNumber(int[] nums) {
        int max;
        int miss=0;
        Arrays.sort(nums);
        int nearr[]=new int[nums.length+1];
        for(int i=0;i<nums.length+1;i++){
            nearr[i]=i;
        }

            for(int k=0;k<nearr.length-1;k++){
                if(nearr[k]!=nums[k]){
                    miss=nearr[k];
                    break;
                }
            }
        return miss;
    }

    public static void main(String[] args) {
        int a[]={0,1};
        System.out.println(missingNumber(a));
    }
}
