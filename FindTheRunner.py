"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[]  of n integers each separated by a space.

Constraints
2<=n<=10
Output Format
-100<=A[i]<=100
Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    sorted_list=sorted(arr)
    i = len(sorted_list)
    while i>0:
        if(sorted_list[i-1]!=sorted_list[i-2]):
            print(sorted_list[i-2])
            break
        i=i-1
    
"""
GptAnswer

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Maksimum skoru bul
    max_score = max(arr)
    
    # Maksimum skoru listeden çıkararak ikinci en büyük skoru bul
    runner_up = max([x for x in arr if x != max_score])
    
    print(runner_up)

"""    
    
    
    
        
    
    
    
            
    
    
        
    
    