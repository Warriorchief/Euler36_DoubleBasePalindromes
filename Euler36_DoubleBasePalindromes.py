#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 20:40:24 2017

@author: christophergreen

Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from numpy import binary_repr

def is_pal(n):
    if str(n) == str(n)[::-1]:
        return True;
    return False;

def main(maximum):
    i=0;
    sumholder=0;
    while i<maximum:
        if is_pal(i) and is_pal(binary_repr(i)):
            print(i,"and its binary form",binary_repr(i),"are both palindromes");
            sumholder+=i;
        i+=1;
    print("sum of the double-base primes below",maximum,"is:",sumholder);
    return sumholder;
    
main(10**6); #--> 20 CORRECT
            
