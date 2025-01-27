public class swap {
    public static void main(String[] args) {
        int a=10;
        int b=30;
        int c=a+b;
        a=c-a;   //subtract the a value from total to get b value and assign into a
        b=c-b;   //subtract the b value from total to get a value and assign into b
        System.out.println("a value is:"+a);
        System.out.println("b value is:"+b);
    }
}
