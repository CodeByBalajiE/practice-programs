import java.util.Scanner;
public class perfectnum {
    public static void main(String[] args) {
        Scanner inp=new Scanner(System.in);
        System.out.println("enter a num");
        int n=inp.nextInt();
        int sum=0;
        for(int i=1;i<n;i++){
            if(n%i==0){//checking factors of n
                sum+=i;
            }
        }
        if(sum==n){
            System.out.println("it is a perfect number");
        }
    }
}
