##    https://www.hackerrank.com/challenges/beautiful-triplets/problem
##
##    Given a sequence of integers s, a triplet (s[i], s[j], s[k]) is beautiful if:
##
##        i < j < k
##        s[j] - s[i] = s[k] - s[j] = d
##
##    Given an increasing sequence of integers and the value of d, count the
##    number of beautiful triplets in the sequence.

##### ##### ##### #####

#   O(n)
#   n is the number of elements in the given sequence

#   Idea:
#       The number of triplets that exist, given a certain starting integer R
#       can be represented as the following:

#       (occurrences of R) * (occurrences of R+d) * (occurrences of R+d+d)

#       With this in mind, we can first build an occurrence table to store the
#       occurrences of each integer in the given array.  Then we iterate over
#       the occurrence table and for each key we check if key+d and key+d+d exist.
#       If they do, we perform the above operation and then add that to the total
#       triplets found.

#   Algo:
#       1. Initialize a dictionary for use as an occurence table => O(1)
#       2. Initialize variable to store the total number of beautiful
#           triplets found => O(1)
#       3. Iterate over the given array => O(|array|)
#               For each integer:
#               increment its count in the dictionary if it exists => O(1)
#               Create its counter if it doesn't => O(1)
#       4. Iterate over the occurrence table => O(|occurrence table|)
#               For each key:
#               initialize a variable to store the number of triplets
#               that begin with that key => O(1)
#               check if key+d and key+d+d exist +=> O(1)
#               if they do increment the local triplet count by the above formula
#               then add the local triplet count to the total triplet count => O(1)
#               if they don't exist, do nothing and go to the next key
#       5. Return total beautiful triplets found => O(1)

##### ##### ##### #####

def beautifulTriplets(d, arr):

    #####

    #   initializing data structures
    
    occurrence_table = dict()
    beautiful_triplets_found = 0
    
    for integer in arr:
        
        try:
            occurrence_table[integer] += 1
            
        except:
            occurrence_table[integer] = 1

    #####

    #   problem solving
            
    for key in occurrence_table:
        
        current_triplets = 0
        
        try:
            current_triplets += (occurrence_table[key] * occurrence_table[key+d] * occurrence_table[key+d+d])
            
        except:
            pass
        
        beautiful_triplets_found += current_triplets
        
    return beautiful_triplets_found
