import java.util.Scanner;
public class lnumofdigit {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter num");
        int num=sc.nextInt();
        System.out.println("Largest digit in a given number is:"+check(num));
    }
    static int check(int num){
        int max=0;
        while(num!=0){
        int a=num%10;
        num=num/10;
        if(a>max)
            max=a;
        }
        return max;
}}
