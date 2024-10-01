from typing import List
from algorithms.mergesort import mergesort

def sort_the_students(score: List[List[int]], k) -> bool:
	return mergesort(score, key=lambda student_lst: -student_lst[k])

if __name__ == "__main__":
	pass