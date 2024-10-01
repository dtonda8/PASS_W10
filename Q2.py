from typing import List
from algorithms.mergesort import mergesort

def sort_the_sentence(s: str) -> bool:
    split_str = s.split(" ")
    new_lst: List[List[str]] = [] # to store [string, index]
    for word_and_idx in split_str:
          new_lst.append([word_and_idx[:-1], word_and_idx[-1]])

    lst = mergesort(new_lst, lambda lst: lst[1])
    
    result: List[str] = []
    for word, idx in lst:
        result.append(word)
    
    return " ".join(result)
	# raise NotImplementedError()


if __name__ == "__main__":
	pass