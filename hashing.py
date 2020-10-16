'''
Quartic Hashing
'''
def hash_quartic(x, tableSize): 
    A = ["-"]*tableSize        # initialise table A

    for k in x:
        i = ((4*k)+7) % tableSize      # h(k) function
        m = i
        count = 0      # initialising counter    

        while A[i] != "-":
            i = (m + (count**4)) % tableSize      # quartic probing function
            count+=1
            if count == tableSize:     # returns the table after [tableSize] as max size of table has reached
                return A

        A[i] = k    # appends key to the table A
    return A

'''
Double Hashing
'''    
def hash_double(y, tableSize):
    B = ["-"]*tableSize # initialise table B

    for k in y:
        i = ((4*k)+7) % tableSize  # h(k) function
        m = i
        count = 0   # initialise counter

        while B[i] != "-":
            i = (m + (count*(17 - (k % 17)))) % tableSize      # h'(k) function 
            count+=1
            if count == tableSize: # returns the table after [tableSize] as max size of table has reached
                return B

        B[i] = k    # appends key to the table B
        
    return B

if __name__ == "__main__":
    sizeOfHashTable = int(input('Enter size of hash table: \n'))
    numList = eval(input('Enter list of numbers (using the form => [19,38,57,76,95,114,133,152,171,190]): \n'))

    print(hash_quartic(numList,sizeOfHashTable), '\n')
    print(hash_double(numList,sizeOfHashTable))
    
