import java.util.Arrays;

public class twopointer {
    public static void main(String[] args) {
        int a[]={0,1,0,3,4,5};
        int i=0;
        int j=i+1;
        int temp;
        while(i<a.length-1) {
            if(a[i]==0){
                temp=a[i];
                a[i]=a[i+1];
                a[i+1]=temp;
                i++;
            }
            if(i==a.length-2){
                i=0;
            }
        }
        System.out.println(Arrays.toString(a));
    }
}
