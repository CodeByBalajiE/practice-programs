    public class insertion {
        static void check(){
            System.out.println("balaji");
        }
        public static void main(String[] args) {
            int a[]={5,3,6,1,2,0};
    //{3,5,6,1,2,0}
            for(int i=1;i<a.length;i++){
                int key=a[i];
                int j=i-1;
                while(a[j]>key){
                    a[j+1]=a[j];
                    System.out.println();
    
                    j--;
                    if(j<0){
                        break;
                    }
                }
                a[j+1]=key;
            }
            for (int nums:a){
                System.out.println(nums);
            }
            check();
        }
