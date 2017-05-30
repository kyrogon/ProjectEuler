#!/usr/bin/env python3

from os.path import abspath
from os.path import pardir
from os.path import dirname


def product(*args):
    result = 1
    for arg in args:
        result *= int(arg)
    return result


def euler008():
    """
    --- Largest product in a series ---
    
    The four adjacent digits in the 1000-digit number that have the 
    greatest product are 9 x 9 x 8 x 9 = 5832.
    
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450
    
    Fin the thirteen adjacent digits in the 1000-digit number that
    have the greatest product.
    What is the value of this product?
    """

    # Set project directory
    pd = abspath(dirname(__file__)+'/'+pardir)
    highest_product = 0

    # Get large number from file
    with open(pd+'/resources/Euler008.txt', 'r') as number_file:
        lines = [line.strip() for line in number_file.readlines()]
        big_num = ''.join(lines)

    # Iterate through number by 13 digit segments
    for end in range(13, len(big_num)-1):
        start = end-13

        new_product = product(*big_num[start:end])
        if new_product > highest_product:
            highest_product = new_product

    print(highest_product)
    return 0



if __name__ == "__main__":
    euler008()