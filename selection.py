A = [64,25,12,22,11, 12,23,24,36,41,32,42,10,16,15]
for i in range(len(A)):   
    min_id = i
    for j in range(i+1, len(A)):
        if A[min_id] > A[j]:
            min_id = j  
    A[i], A[min_id] = A[min_id], A[i]
print("Sorted Array")
for i in range(len(A)):
    print("%d" %A[i],end=" ")