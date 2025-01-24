public class SumOfNumbers {
public static void main(String[] args) {
int n = 5; // The number to sum 
        int sum = 0; // Variable to store the total sum

        // Use a loop to add numbers from 1 to n
        for (int i = 1; i <= n; i++) {
            sum += i; // Add current number to sum
        }
        System.out.println("The sum of numbers from 1 to " + n + " is: " + sum);
    }
}
