'''
[3/15/2012] Challenge #25 [easy]
In an election, the person with the majority of the votes is the winner. Sometimes due to similar number of votes,
there are no winners. Your challenge is to write a program that determines the winner of a vote, or shows that there
are no winners due to a lack of majority.
'''
import collections
lst = ["a", "b", "a",'c',"b","a",'b','a','c','b','a','a']

def challenge25(l):
    count_ballots = collections.Counter(lst)

    # 2 best
    best_candidates = count_ballots.most_common(2)

    # if both got the same # of votes
    if best_candidates[0][1] == best_candidates[1][1]:
        return None

    elif best_candidates[0][1] > best_candidates[1][1]:
        winner_so_far = best_candidates[0]
    else:
        winner_so_far = best_candidates[1]


    if winner_so_far[1] >= len(lst)/2:
        print "The winner is candidate {}.".format(winner_so_far[0])
        return winner_so_far[0]
    else:
        return None

if __name__ == "__main__":
    challenge25(lst)