import java.util.Scanner;

public class mornafte {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter a num");
        int a=sc.nextInt();
        System.out.println(check(a));
    }
    static String check(int a){
        if(a%3==0 && a%4==0)
            return "Good Morning";
        if(a%4==0 && a%3!=0)
            return "Good Afternoon";
        if(a%3==0 && a%4!=0)
            return "Good Evening";
        else{
            return "Good Night";
    }}
}
