public class flocc {
    public static void main(String[] args) {
        int a[]={2,5,7,5,8};
        int i=0;
        int j=a.length-1;
        int targ=5;
        int c=0;
        while(i<j){
            if(a[i]==targ){
                System.out.println(i);
                c+=1;
            }
            else {
                i++;
            }
            if(a[j]==targ){
                System.out.println(j);
                c+=1;
            }
            else {
                j--;
            }
            if(c==2){
                break;
            }
        }
    }
}
