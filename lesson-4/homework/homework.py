# answers (https://pynative.com/python-if-else-and-for-loop-quiz/): D B B C C A B B B B B A A C A C B B B D B B B A B

# break quits the loop, and the 'else' below is not performed, while the 'continue' just skips specific iteration. continue should be used cautiously, though, as it might lead to infinite loop if the update statement is after it, instead of before (I personally had many such mistakes). 

# for loop is for iterators (.begin() and .end() in C++). It iterates through list, tuple, dictionary (keys by default), or any other iterators, like zip(), or the popular 'enumerate' and 'range'. while loop is much broader, it can do more things than just iterating. We use condition, and iterate till it is false. for loop is 'subset' of while loop, using 'next()' call for iteration, and using the existence of next element as condition. 

# Handling nested loop is so abstract question.
# for row in arr:
#     for i in row:
#         ...
# while ...:
#     while ...:
# I'd give insertion sort as example, which should be something like:
# for i in range(1, len(arr)):
#     for j in range(i - 1, -1, -1):
#         if arr[j] > arr[j+1]:
#             temp = arr[j+1]
#             arr[j+1] = arr[j]
#             arr[j] = temp
#         else:
#             break


# Homework:

from random import randint
from random import choice
import re

def uncommon(l1, l2):
    """Doesn't work, because repeat is allowed. 
    Fix is counting and appending, 
    implemented in the comment below."""
    # l = list(set(l1) ^ set(l2)); s = l1 + l2; r = [sum(s == i) for i in l]; ans = []
    # for i in range(len(l)):
    #     for j in range(r[i]):
    #         ans.append(l[i])
    # return ans
    return list(set(l1) ^ set(l2))

def uncommonTheHardWay(l1, l2):
    lst = []
    for i in l1:
        if i not in l2:
            lst.append(i)
    for i in l2:
        if i not in l1:
            lst.append(i)
    return lst


def square(n):
    return [i**2 for i in range(1, n)]

def printSquares(n):
    for i in square(n):
        print(i)


def underscore(s):
    used, vow = [], ['a', 'e', 'i', 'o', 'u']
    i, j, ans, l = 2, 0, s, len(s)
    while i < l - 1:
        if not (s[i] in vow or s[i] in used):
            ans = ans[:i+j+1] + '_' + ans[i+j+1:]
            used.append(s[i])
            j += 1
        else:
            i += 1
            continue
        i += 3
    return ans

print(underscore("abcabcdabcdeabcdefabcdefg")) # abc_abcd_abcdeab_cdef_abcdefg


def randomGame():
    while True:
        num = randint(1, 100)
        for i in range(10):
            n = int(input("Select number (0-100): "))
            if n < num:
                print("Too low!")
            elif n > num:
                print("Too high!")
            else:
                print("You guessed it right!")
                return
        else:
            again = input("You lost. Want to play again? ")
            if again not in ['y', 'Y', 'yes', 'YES', 'ok']:
                break

def winTheRandomGame(): # simple binary search
    l, r = 0, 101
    while r > l:
        m = (r + l) // 2
        print(m)
        res = input()
        if res == "Too low":
            l = m + 1
        elif res == "Too high":
            r = m - 1
        else:
            break


def passwordChecker():
    while True:
        p = input()
        c1 = len(p) >= 8
        c2 = len(re.findall(r"[A-Z]", p)) > 0
        if c1 and c2:
            print("Password is strong.")
            break
        if not c1:
            print("Password is too short.")
        if not c2:
            print("Password must contain an uppercase letter.")


def primes(n = 100): # Sieve O(n*log(n))
    l = [True] * n
    l[0] = False
    for i in range(n//2):
        if l[i]:
            for j in range(2*i+1, n, i+1):
                l[j] = False
    for i in range(n):
        if l[i]:
            print(i+1)
    return [i+1 for i in range(n) if l[i]]

def primesTheShortWay(n = 100): # O(n**2)
    for i in range(2, n+1):
        if (all(i % t != 0 for t in range(2, i))):
            print(i)

def primesTheNestedLoop(n = 100): # nested loops (no usage of 'all'), but instead nested loops as explicitly asked in the question
    for i in range(2, n+1):
        b = True
        for t in range(2, i):
            b = b and i % t != 0
            if not b:
                break
        if b:
            print(i)


# Bonus Challenge:

def rps():
    options = ["rock", "paper", "scissors"]
    score = [0, 0]
    win = lambda x, y: x == "rock" and y == "scissors" or x == "paper" and y == "rock" or x == "scissors" and y == "paper"
    while all(s < 5 for s in score):
        c = choice(options)
        u = input("rock/paper/scissors? ").lower()
        if u == c:
            print("Tie")
        elif win(c, u):
            score[0] += 1
            print("Computer won", score)
        elif win(u, c):
            score[1] += 1
            print("You won", score)
        else:
            print("Invalid input")
    if score[0] == 5:
        print("Computer is the winner!", score)
    else:
        print("You are the winner!", score)





