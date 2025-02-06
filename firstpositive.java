import java.util.Arrays;

public class firstpositiive {
    public static void main(String[] args) {
        int a[]={4,3,2,7,1};
        int positive =1;
        int i=0;
        while(i<a.length){
            if(a[i]==positive){
                positive++;
                i=0;
            }
          else{
            i++;

        }

            }
        if(i<=a.length){
            System.out.println(positive);

        }



    }
}
