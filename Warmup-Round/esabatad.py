#!/usr/bin/env python3

# PROBLEM Last year, a research consortium had some trouble with a distributed database system that sometimes lost
# pieces of the data. do not need to read or understand that problem in order to solve this one!
#
# The consortium has decided that distributed systems are too complicated, so they are storing B bits of important
# information in a single array on one awesome machine. As an additional layer of security, they have made it
# difficult to obtain the information quickly; the user must query for a bit position between 1 and B, and then they
# receive that bit of the stored array as a response.
#
# Unfortunately, this ultra-modern machine is subject to random quantum fluctuations! Specifically, after every 1st,
# 11th, 21st, 31st... etc. query is sent, but before the response is given, quantum fluctuation causes exactly one of
# the following four effects, with equal probability:
#
# 25% of the time, the array is complemented: every 0 becomes a 1, and vice versa. 25% of the time, the array is
# reversed: the first bit swaps with the last bit, the second bit swaps with the second-to-last bit, and so on. 25%
# of the time, both of the things above (complementation and reversal) happen to the array. (Notice that the order in
# which they happen does not matter.) 25% of the time, nothing happens to the array. Moreover, there is no indication
# of what effect the quantum fluctuation has had each time. The consortium is now concerned, and it has hired you to
# get its precious data back, in whatever form it is in! Can you find the entire array, such that your answer is
# accurate as of the time that you give it? Answering does not count as a query, so if you answer after your 30th
# query, f or example, the array will be the same as it was after your 21st through 30th queries.
#
#
# INPUT and OUTPUT
# This is an interactive problem. You should make sure you have read the information in the
# Interactive Problems section of our FAQ.
#
# Initially, your program should read a single line containing two integers T and B: the number of test cases and the
# number of bits in the array, respectively. Note that B is the same for every test case.
#
# Then, you need to process T test cases. In each case, the judge begins with a predetermined B-bit array; note that
# this array can vary from test case to test case, and is not necessarily chosen at random. Then, you may make up to
# 150 queries of the following form:
#
# Your program outputs one line containing a single integer P between 1 and B, inclusive, indicating which position
# in the array you wish to look at. If the number of queries you have made so far ends with a 1, the judge chooses
# one of the four possibilities described above (complementation, reversal, complementation + reversal, or nothing),
# uniformly at random and independently of all other choices, and alters the stored array accordingly. (Notice that
# this will happen on the very first query you make.) The judge responds with one line containing a single character
# 0 or 1, the value it currently has stored at bit position P, or N if you provided a malformed line (e.g.,
# an invalid position). Then, after you have made as many of the 150 queries above as you want, you must make one
# more exchange of the following form:
#
# Your program outputs one line containing a string of B characters, each of which is 0 or 1, representing the bits
# currently stored in the array (which will not necessarily match the bits that were initially present!) The judge
# responds with one line containing a single letter: uppercase Y if your answer was correct, and uppercase N if it
# was not (or you provided a malformed line). If you receive Y, you should begin the next test case, or stop sending
# input if there are no more test cases. After the judge sends N to your input stream, it will not send any other
# output. If your program continues to wait for the judge after receiving N, your program will time out, resulting in
# a Time Limit Exceeded error. Notice that it is your responsibility to have your program exit in time to receive a
# Wrong Answer judgment instead of a Time Limit Exceeded error. As usual, if the memory limit is exceeded,
# or your program gets a runtime error, you will receive the appropriate judgment.

# SOLUTION
# While I still have queries or haven't found all numbers, I update my numberList by asking for numbers, then
# checking for suitable candidates to check if the list has been complemented or not or reverse or not (or both).
# If I have suitable candidates, I check if they've been modified, if yes, change the list accordingly.

# PROBLEMS
# 1. My main while condition is not correct, it doesn't match the code logic.
# 2. The number of bits I ask for each iteration change, but the rate of change is wrong. I reduce them by 2
#   everytime, which won't work. The correct answer is something on the lines of - 10, 8, 8, ...
# 3.
import sys


# Inputting non-index friendly values
def update(start):
    global elem, loc, B, fin
    count = 1
    ind = 0
    mult = start - 6
    rem = 6
    while mult >= 0:
        rem += 10
        mult -= 10
    for i in range(start, start + fin):
        if count < rem:
            ind = i
        else:
            ind = B - (i % rem)
        print(ind)
        loc[ind - 1] = 1
        sys.stdout.flush()
        s = int(input())
        elem[ind - 1] = s
        count += 1
        fin -= 2
        if fin <= 0:
            fin = 10


# Check if the sequence has been complemented
def check_complement(val):
    global elem
    print(val + 1)
    sys.stdout.flush()
    s = int(input())
    if elem[val] == s:
        return False
    else:
        return True


# Check if the sequence has been reversed
def check_reverse(val):
    global elem
    print(val + 1)
    sys.stdout.flush()
    s = int(input())
    if elem[val] == s:
        return False
    else:
        return True


# Select values through which we can identify if the sequence has been complemented or not else return -1
def sel_complement(s, l, st):
    global elem
    start = s - 1
    last = l - 1
    step = st

    while step > 0:
        if elem[start] == elem[last]:  # If equals, you can check for complement
            return start
        start += 1
        last -= 1
        step -= 1
    return -1


# Select values through which we can identify if the sequence has been reversed or not else return -1
def sel_reverse(s, l, st):
    global elem
    start = s - 1
    last = l - 1
    step = st

    while step > 0:
        if elem[start] != elem[last]:  # If true, you can check for reverse
            return start
        start += 1
        last -= 1
        step -= 1
    return -1


# Select complement and reverse values, then check if the sequence has been complemented/reversed or not.
# If yes, change the local list
def dostuff():
    global B, query, elem, loc
    comp = sel_complement(1, B,
                          10)  # Selects the value that won't change on reverse, thus it can tell us about complement

    isComp = False
    if comp != -1:
        isComp = check_complement(comp)
        query += 1

    if isComp:
        for i in range(0, B):
            if loc[i] == 1:
                if elem[i] == 1:
                    elem[i] = 0
                else:
                    elem[i] = 1

    rev = sel_reverse(1, B, 10)  # Selects the value that will change on reverse
    isRev = False
    if rev != -1:
        isRev = check_reverse(rev)
        query += 1

    if isRev:
        for i in range(0, (int(B / 2))):
            if loc[i] == 1:
                if elem[i] != elem[B - 1 - i]:
                    temp = elem[i]
                    elem[i] = elem[B - 1 - i]
                    elem[B - 1 - i] = temp


# Initial Values
T = 0
B = 0
elem = [0]
loc = [0]
fin = 10
query = 0


# For each test case, while queries left and all elements not found - keep updating, checking, and modifying
def main():
    global T
    global B, elem, loc, query
    T, B = map(int, input().split())
    for test in range(T):
        query = 1
        elem = [0] * B
        loc = [0] * B
        increment = 1
        while query < 150 and 0 in loc:
            update(list(loc).index(0) + 1)
            query += 10
            dostuff()
            increment += 10

        # if (query + 1 % 11) < 9:
        #     dostuff()

        resStr = ""
        for val in elem:
            resStr += str(val)
        print(resStr)
        sys.stdout.flush()
        a = input()
        if a == "Y":
            continue
        else:
            break


if __name__ == '__main__':
    main()
