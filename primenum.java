public class primenum {

//logic 1 for primenum
  public static void main(String[] args) {
        int num=100003 ;
        int count=0;
        for(int i=1;i<=num;i++){
            if(num%i==0){
                count++;
            }
        }
        if(count==2){
            System.out.println("it is prime");
        }
        else{
            System.out.println("it is not prime");
        }
    }
//logic 2 for primenum 
  public static boolean isprime(int num){
      if(num<2){
          return false;
      }
      for(int i=2;i<=Math.sqrt(num);i++){

          if(num%i==0){
              return false;
          }
      }
      return true;
  }

    public static void main(String[] args) {
        if(isprime(100003 )){
            System.out.println("prime num");
        }
        else{
            System.out.println("it is not prime");
        }
    }
}
