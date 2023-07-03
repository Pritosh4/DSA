n = input()
i = 0
j = 1
lps = [0]*len(n)
while j < len(n):
    if n[i] == n[j]:
        i += 1
        lps[j] = i
        j += 1
    else:
        if i != 0:
            i = lps[i - 1]
        else:
            lps[j] = 0
            j += 1
print(lps)
