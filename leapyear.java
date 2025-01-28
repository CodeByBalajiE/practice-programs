import java.util.*;
public class leapyear {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        System.out.println("enter the year");
        int a =input.nextInt();
        if(a%4==0 && a%100!=0 ||a%400==0){ //A leap year is divisible by 4 and not divisible by 100 or divisible by 400.
            System.out.println("this is leap year");
        }
        else{
            System.out.println("this is not a leap year");
        }
    }
}
