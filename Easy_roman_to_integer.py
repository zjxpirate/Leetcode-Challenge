

dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def result(A):
    output = 0
    output1 = 0
    output2 = 0
    for i in range(len(A) - 1):
        output1 += dict[A[i]]
        if dict[A[i+1]] > dict[A[i]]:
            output2 += dict[A[i]]

    output1 += dict[A[-1]]
    output = output1 - 2 * output2
    return output



input = 'MCMXCIV'


print(result(input))





































