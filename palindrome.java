import java.util.Scanner;
public class palindrome {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter the string to check if it is a palindrome");
        String a=s.nextLine();
        String b = a.toLowerCase().replaceAll("[ ,: ]","");

        String reversed="";
        for(int i=b.length()-1;i>=0;i--){
            reversed+=b.charAt(i); //reverse the string
        }
        System.out.println(reversed);
        if(reversed.equals(b)){
            System.out.println("it is palindrome");
        }
        else{
            System.out.println("not palindrome");
        }

    }
}
