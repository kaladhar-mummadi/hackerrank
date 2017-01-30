t = int(input())

for _ in range(t):
    word = list(input())
    start = -1
    for i in range(0, len(word)-1):
        if word[i] < word[i+1]:
            start = i
    if start == -1:
        print("no answer")
        continue
    end = -1
    for i in range(start+1, len(word)):
        if word[start] < word[i]:
            end = i
    word[start], word[end] = word[end], word[start]
    word[start+1:] = sorted(word[start+1:])
    print("".join(word))