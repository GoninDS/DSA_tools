def print_merge(array):
    print('Result after merge')
    for l in range(n):
        print(array[l], end=" ")
    print('\n')

def merge(array, p, q, r):
    nl = q - p + 1
    nr = r - q

    L = [0] * (nl)
    R = [0] * (nr)

    for i in range(0, nl):
        L[i] = array[p + i]

    for j in range(0, nr):
        R[j] = array[q + j + 1]

    i = 0
    j = 0
    k = p

    while (i < nl and j < nr):
        if (L[i] <= R[j]):
            array[k] = L[i]
            i += 1
        else: 
            array[k] = R[j]
            j += 1
        k += 1

    while (i < nl):
        array[k] = L[i]
        i += 1
        k += 1

    while (j < nr):
        array[k] = R[j]
        j += 1
        k += 1

    print_merge(array)


def print_values_return(p, r, depth):
    print('Mergesort called with:')
    print('p: ' + str(p))
    print('r: ' + str(r))
    print('q: NA')
    print('depth:' + str(depth))

def print_values(p, r, q, depth):
    print('Mergesort called with:')
    print('p: ' + str(p))
    print('r: ' + str(r))
    print('q: ' + str(q))
    print('depth:' + str(depth))

    for i in range(n):
        print(array[i], end=" ")

    print('\n')

def mergesort(array, p, r, depth):
    if (p >= r):
        print_values_return(p, r, depth)
        return None
    
    q = (p + r) // 2

    print_values(p, r, q, depth)
    
    mergesort(array, p, q, depth + 1)
    mergesort(array, q + 1, r, depth + 1)
    merge(array, p, q, r)


array = ['G', 'V', 'A', 'N', 'R', 'O', 'P', 'U']
n = len(array)
print("Without sorting")

for i in range(n):
    print(array[i], end=" ")
print('\n')

mergesort(array, 0, n-1, 1)

print("Sorted")
for i in range(n):
    print(array[i], end=" ")