# PASS_W10

### Q1: Sort the Students by Their Kth Score (from [here](https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/))
There is a class with m students and `n` exams. You are given a 0-indexed `m` x `n` integer matrix score, where each row represents one student and `score[i][j]` denotes the score the `i`th student got in the `j`th exam. The matrix score contains distinct integers only.

You are also given an integer `k`. Sort the students (i.e., the rows of the matrix) by their scores in the `k`th (0-indexed) exam from the highest to the lowest.

Return the matrix after sorting them in descending order of the score in the `k`th exam.


Example 1:
**Input**: `score` = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], `k` = 2
**Output**: [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
Explanation:  
- The student with index 1 scored 11 in exam 2, which is the highest score, so they got first place.
- The student with index 0 scored 9 in exam 2, which is the second highest score, so they got second place.
- The student with index 2 scored 3 in exam 2, which is the lowest score, so they got third place.

Example 2:  
**Input**: `score` = [[3,4],[5,6]], `k` = 0
**Output**: [[5,6],[3,4]]
Explanation:  
- The student with index 1 scored 5 in exam 0, which is the highest score, so they got first place.
- The student with index 0 scored 3 in exam 0, which is the lowest score, so they got second place.

Note: It is guaranteed that `k` is a valid index  

---
### Q2: Sorting the Sentence (from [here](https://leetcode.com/problems/sorting-the-sentence/description/))
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence `s` containing no more than 9 words, reconstruct and return the original sentence.

Note: It is guaranteed that there is at most 10 words  


Example 1:
**Input**: `s` = "is2 sentence4 This1 a3"  
**Output**: "This is a sentence"  
Explanation: Sort the words in `s` to their original positions "This1 is2 a3 sentence4", then remove the numbers.  

Example 2:  
**Input**: `s` = "Myself2 Me1 I4 and3"  
**Output**: "Me Myself and I"  
Explanation: Sort the words in `s` to their original positions "Me1 Myself2 and3 I4", then remove the numbers.  

---

### Testing you algorithm
- To run tests, open terminal then:
```sh
python3 run_tests.py # and follow command line instructions
```

- If you encounter errors with the above, make sure that at least python runs on terminal
```sh
python3
```

- You may be directed to Microsoft Store (Windows), if so install python from there
- For if issues persist on Mac,  see this: https://docs.python-guide.org/starting/install3/osx/
