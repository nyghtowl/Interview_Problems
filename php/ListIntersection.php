<?php

/**
 * List Intersection
 *
 * Basic Variant Question: Given two lists of strings, find the intersection
 * of the two lists.
 *
 * Sample Input:
 *  $a1 = ['dog', 'cat', 'egg']
 *  $a2 = ['cat', 'dog', 'chicken']
 *
 * Output:
 *  $out = ['dog', 'cat']
 */


/**
 * Solution A: Brute force looping - O(n^2) or O(n*m)
 *
 * @param array $listA
 * @param array $listB
 *
 * @return null
 */
function findListIntersect($listA, $listB)
{
    $output = [];
    foreach ($listA as $itemA) {
        foreach ($listB as $itemB) {
            if (strcmp($itemA, $itemB) === 0) {
                echo "$itemA\r\n";
            }
        }
    }
}

/**
 * Solution B: Hashing and counts dups - O(n)
 *
 * Note: The reason this solution is considered O(n) is because PHP associative
 *  arrays are implemented as HashTables.
 *
 * For more information:
 * http://stackoverflow.com/questions/2350361/how-is-the-php-array-implemented-on-the-c-level
 *
 * @param array $listA
 * @param array $listB
 *
 * @return null
 */
function findListIntersectWithDupe($listA, $listB)
{
    $output = [];

    foreach ($listA as $item) {
        isset($output[$item]) ? $output[$item]++ : $output[$item] = 0;
    }

    foreach ($listB as $item) {
        isset($output[$item]) ? $output[$item]++ : $output[$item] = 0;
    }

    foreach ($output as $element => $count) {
        if ($count > 0) {
            echo "$element => $count\r\n";
        }
    }
}

/**
 *  Test section
 */

// Set up input
$inputA = ['dog', 'cat', 'egg'];
$inputB = ['cat', 'dog', 'chicken'];
$inputWithDupeA = ['cat', 'dog', 'dog', 'chicken'];
$inputWithDupeB = ['bird', 'bird', 'dog', 'chicken'];

// Test 1: Basic intersect
findListIntersect($inputA, $inputB);

// Test 2: Basic intersect, improved solution
findListIntersectWithDupe($inputA, $inputB);

// Test 3: Intersect with duplicates in both inputs
findListIntersectWithDupe($inputWithDupeA, $inputWithDupeB);
