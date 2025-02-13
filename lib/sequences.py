#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = [0, 1]
    for _ in range(length-2):
        sequence.append(sequence[-1] + sequence[-2])
    print(sequence[:length])
    pass

print(print_fibonacci(10))