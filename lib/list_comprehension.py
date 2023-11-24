#!/usr/bin/env python3

def return_evens(num_list):
   return [ n for n in num_list if n % 2 == 0]
num_list = [0, 1, 3, 5, 7, 8, 9]
print(return_evens(num_list))


def make_exclamation(sentence_list):
   return [str + "!" for str in sentence_list]
pass
sentence_list = ["Hello", "I'm doing great", "Python is fun"]
result = make_exclamation(sentence_list)
print(result)