import java.util.*;
public class recursion {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        int n=input.nextInt();
        System.out.println(recursion.factorial(n));;
    }
    public static int factorial(int n){
        //base case
        if(n==1){
            return 1;
        }
        //recursive case 
        else{
            return n*factorial(n-1);
        }
    }
}
