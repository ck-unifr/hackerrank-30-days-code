#https://www.hackerrank.com/challenges/30-review-loop/problem

# Input Format
#
# The first line contains an integer T (the number of test cases).
# Each line i of the T subsequent lines contain a String S.


# Output Format
#
# For each String S_j (where 0 <= j <= T-1), print S_j's even-indexed characters,
# followed by a space, followed by S_j's odd-indexed characters.


T = int(input().strip())
S = []
for i in range(T):
    sentence = input().strip()
    S.append(sentence)

for sentence in S:
    odd_sentence = ''
    even_sentence = ''
    for i, char in enumerate(sentence):
        if (i+1) % 2 != 0: odd_sentence += char
        else: even_sentence += char
    print('{} {}'.format(odd_sentence, even_sentence))
