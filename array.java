public class array {
    public static void main(String[] args) {
        int[] a={4,1,2,1,2};
        int result=0;
        for(int num:a){
            result^=num;//x or operation to get non repeating interger
        }
        System.out.println(result);
        }

    }


