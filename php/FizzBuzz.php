<?php

/**
 * Traditional FizzBuzz
 *
 * Question: Print out the numbers 1 to n with the following caveats:
 *
 *  - If the number is divisible by 3, print Fizz
 *  - If the number is divislble by 5, print Buzz
 *  - If the number is divisible by 3 and 5, print FizzBuzz
 *
 *  Input: Max number to print to, n
 *
 *  Output: Printed list of numbers
 */

function fizzBuzz($n) {
    for ($i = 1; $i <= $n; $i++) {
        $print = '';
        if ($i % 3 == 0) {
            $print .= 'Fizz';
        }
        if ($i % 5 == 0) {
            $print .= 'Buzz';
        }
        if (empty($print)) {
            $print = $i;
        }

        echo "$print\r\n";
    }
}

fizzBuzz(100);
