'''
Python program to create string permuations

How it works
1) Iterate through the initial string e.g., 'abc'.
2) For each character in the initial string, set aside that character and get a list of all permutations of the string that's left. 
3) Once you have the list from step 2, add each element from that list to the character from the initial string, and append the result to our list of final results. 
4) Return the list of final results.

'''

def permute(string):
    out = []

    if len(string) == 1:
        out = list(string)

    else:
        for i in range(len(string)):
            for perm in permute(string[:i]+string[i+1:]): # everying except current index, ie find the permtation for the rest
                out.append(string[i] + perm)
    
    return out

string = 'abc'
permutations = permute(string)

print('Permutations for "{}" are:\n\n{}'.format(string, ' '.join(permutations)))

'''
OUTPUT

Permutations for "abc" are:

abc acb bac bca cab cba
'''