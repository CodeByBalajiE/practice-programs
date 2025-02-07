import java.util.Scanner;

public class numgroup {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter a number");
        int nums=sc.nextInt();
        check(nums);
    }
    static void check(int num){
        if(num>50)
            System.out.println("ABOVE FIFTY CATEGORY");
        if(num<40)
            System.out.println("BELOW FORTY CATEGORY");
        if(num>40&&num<50)
            System.out.println("BETWEEN 40 AND FIFTY CATEGORY");
    }
}
