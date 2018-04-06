#!/bin/python3
# Grading students challenge

def answer(grades):
	return [(lambda x: 5 * (1 + x//5) if (x > 37 and ((x%5) > 2)) else x )(x) for x in grades]

if __name__ == '__main__':
	grades = [73, 67, 38, 33]
	print(answer(grades))