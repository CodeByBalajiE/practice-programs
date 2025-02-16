//remove value 10 and move zeros to right
import java.util.Arrays;
import java.util.Scanner;

public class arrr {
    public static void main(String[] args) {
        int a[]={1,10,10,2};
        for(int i=0;i<a.length;i++){
            if(a[i]==10){
                a[i]=0;
            }
        }
        int i=0;
        for(int j=0;j<a.length;j++){
            if(a[j]!=0){
                int temp=a[i];
                a[i]=a[j];
                a[j]=temp;
                i++;
            }
        }
        System.out.println(Arrays.toString(a));
    }
}
