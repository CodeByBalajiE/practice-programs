import java.util.Scanner;

public class sumofdigits {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter a num");
        int a=sc.nextInt();
        int b=0;
        int sum=0;
        while(a>0){
            b=a%10;
            sum+=b;
            a=a/10;
        }
        System.out.println(sum);
    }
}
