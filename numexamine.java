import java.util.Scanner;
public class numexamine {
    public static void main(String []args) {
        Scanner input=new Scanner(System.in);
        System.out.println("Enter a number to check");
        int a= input.nextInt();
        if(a%27==0)//check if a num is multiple of 7
            { //if num is evenly divided it also a multiple of 27 factor
            System.out.println("It is a multiple of 27 and its evenly divided by 27");
        }
            else{
                System.out.println("it is not multiple of 27 and not evenly divided by 27");
            }
    }
}


