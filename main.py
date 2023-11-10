import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[:-1], T)))


def fast_MED(S, T, MED={}):
    if (S, T) in MED.keys():
        return MED[(S, T)]
    else:
        if (S == ""):
            MED[(S, T)] = len(T)
        elif (T == ""):
            MED[(S, T)] = len(S)
        else:
            if (S[0] == T[0]):
                MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
            else:
                MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED), fast_MED(S[:-1], T, MED))
    return MED[(S, T)]

def fast_align_MED(S, T, MED={}):
    if (S, T) in MED.keys():
        return MED[(S, T)]
    else:
        if (S == ""):
            MED[(S, T)] = (len(T), ('-' * len(T), T))
        elif (T == ""):
            MED[(S, T)] = (len(S), (S, '-' * len(S)))
        else:
            if (S[0] == T[0]):
                temp = fast_align_MED(S[1:], T[1:], MED)
                MED[(S, T)] = (temp[0], (S[0] + temp[1][0], T[0] + temp[1][1]))
            else:
                
                insertion = fast_align_MED(S, T[1:], MED)
                deletion = fast_align_MED(S[1:], T, MED)
                substitution = fast_align_MED(S[:-1], T, MED)

                if insertion[0] <= deletion[0] and insertion[0] <= substitution[0]:
                    MED[(S, T)] = (1 + insertion[0], ('-' + insertion[1][0], T[0] + insertion[1][1]))
                elif deletion[0] <= insertion[0] and deletion[0] <= substitution[0]:
                    MED[(S, T)] = (1 + deletion[0], (S[0] + deletion[1][0], '-' + deletion[1][1]))
                else:
                    MED[(S, T)] = (2 + substitution[0], (S[0] + substitution[1][0], T[0] + substitution[1][1]))
        
        return MED[(S, T)]

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
