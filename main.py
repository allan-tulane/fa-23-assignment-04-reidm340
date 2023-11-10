import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for inss, deletions and substitutions
    if (S == ""):
        return len(T)
    
    elif (T == ""):
        return len(S)
    
    else:
        if (S[0] == T[0]):
            return MED(S[1:], T[1:])
        else:
            return (1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[:-1], T)))


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
                ins = fast_align_MED(S, T[1:], MED)
                rem = fast_align_MED(S[1:], T, MED)
                sub = fast_align_MED(S[:-1], T, MED)

                if ins[0] <= rem[0] and ins[0] <= sub[0]:
                    MED[(S, T)] = (1 + ins[0], ('-' + ins[1][0], T[0] + ins[1][1]))
                elif rem[0] <= ins[0] and rem[0] <= sub[0]:
                    MED[(S, T)] = (1 + rem[0], (S[0] + rem[1][0], '-' + rem[1][1]))
                else:
                    MED[(S, T)] = (2 + sub[0], (S[0] + sub[1][0], T[0] + sub[1][1]))
        
        return MED[(S, T)]

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
