import numpy as np 


def min_edit_distance(word1,word2):

    w_1_length = len(word1) # let's say word_1 of total length n 
    w_2_length = len(word2) # let's say word_2 of total length m 

    # A is matrix of shape of words length 
    A = np.zeros((w_1_length+1,w_2_length+1),dtype=int)   
    B = np.zeros((w_1_length+1,w_2_length+1),dtype=object) 

    word1_list = list(word1)
    word2_list = list(word2)
    
    ''' Now coming to min edit distance we will update each and every '''
    A[0,0] = 0
    for n in range(1,w_1_length+1): # row 
        for m in range(1,w_2_length+1): # column 
                    A[n][0] = n
                    A[0][m] = m

    '''Matrix with the annotation of characters'''
    B[0,0] = 0
    for g in range(1,w_1_length+1): # row 
        for f in range(1,w_2_length+1): # column 
                    B[g][0] = word1[g-1]
                    B[0][f] = word2[f-1]

    '''Computing min_edit_distance'''
    for n in range(1,w_1_length+1): # row 
        for m in range(1,w_2_length+1): # column
            if word1[n-1] == word2[m-1]:
                cost = 0
            else:
                cost = 1


            A[n,m] = min(
                A[n - 1, m] + 1,  # deletion
                A[n, m - 1] + 1,  # insertion
                A[n - 1, m - 1] + cost  # substitution
            )
    value = A[w_1_length,w_2_length]

    return A,B, w_1_length, w_2_length, value

word1 = input("please enter word1:")
word2 = input("please enter word2:")

A,B, w_1_length, w_2_length, value = min_edit_distance(word1,word2)

print("first word character enumerated as :")
for a,n in enumerate(word1):
    print(f"{a}:{n}")
print("*" * 50)
print("Second word character enumerated as :")
for b,m in enumerate(word2):
    print(f"{b}:{m}") 
print("*" * 50 + ' integer valued Matrix ' + "*" * 50)
print("Matrix A:")
print(f"{A}")
print("*" * 50 + ' Annoted Matrix ' + "*" * 50)
print("Matrix B:")
print(f"{B}")
print("*" * 50 + ' Length of words ' + "*" * 50)
print("Length of both words")
print(f"Length of first word  : {w_1_length}")
print(f"Length of Second word  : {w_2_length}")
print("*" * 50 + ' Finalized distance ' + "*" * 50)
print(f"The min distance between word1 and word2 is {value}")