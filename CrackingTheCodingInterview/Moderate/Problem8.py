'''
Created on Jul 3, 2015

@author: Debanjan Mahata
'''

def sequence_with_largest_sum(seq):
    max_sum = 0
    s = 0
    max_sequence = []
    for i in range(len(seq)):
        s += seq[i]
        max_sequence.append(seq[i])
        if max_sum < s:
            max_sum = s
        else:
            if s < 0:
                s = 0
                max_sequence = []
                
    return max_sum, max_sequence


if __name__ == "__main__":
    seq = [2,3,-8,-1,2,4,-2,3]
    print sequence_with_largest_sum(seq)
