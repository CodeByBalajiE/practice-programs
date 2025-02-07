import java.util.Scanner;

public class season {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter A Number Of Month To Check The Season");
        int a=sc.nextInt();
        if(a<1&&a>12){
            System.out.println("Invalid Month Enterd");
        }
        if(a==3 |a==4|a==5){
            System.out.println("Spring Season");
        }
        if(a==6|a==7|a==8){
            System.out.println("Summer Season");
        }
        if(a==9|a==10|a==11){
            System.out.println("Autumn Season");
        }
        if(a==12|a==1|a==2){
            System.out.println("Winter Season");
        }
    }
}

