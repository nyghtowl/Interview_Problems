// Fibonacci - each number equals the sum of the two preceding numbers.

// Fn = Fn-1 + Fn-2

// Input: the point in the sequence to take a fibonnaci number
// Output: the fibonnaci number at the point in a sequence starting at 0

// Ex: 
// At position 0 the Fib number is 0. 
// At position 4 the Fib number is 3 (adding 1, 2 which are the numbers before)
import java.util.Scanner;
import java.util.Arrays;

public class Fibonacci
{
    public static void main( String[] args)
    {
        Scanner keyboard = new Scanner(System.in);

        System.out.print("Enter at what place in the fibonnaci sequence do you want to see the number: ");
        int position = keyboard.nextInt();

        int result[];
        if (position < 2) {
            result = new int[position+2];
        }
        else {
            result = new int[position+1];
        }

        int before_val = 0;
        int after_val = 1;
        int counter = 0;
        int temp = 0;
        result[0] = before_val;
        result[1] = after_val;

        do 
        {
            counter++;
            result[counter] = after_val;
            temp = before_val + after_val;
            before_val = after_val;
            after_val = temp;
            
        } while (counter < position);

        // System.out.println (Arrays.toString(result));

        System.out.println(result[position]);

    }
}