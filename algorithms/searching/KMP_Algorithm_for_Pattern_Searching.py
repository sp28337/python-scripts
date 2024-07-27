# KMP Algorithm for Pattern Searching
text = "лилила"
a = "лилилось лилилась"
m = len(text)
n = len(a)


p = [0] * len(text)
j = 0
i = 1
while i < len(text):
    if text[j] == text[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j - 1]
print(p)


i, j = 0, 0
while i < n:
    if a[i] == text[j]:
        i += 1
        j += 1
        if j == m:
            print('Образ найден')
            break
    else:
        if j > 0:
            j = p[j - 1]
        else:
            i += 1

if i == n:
    print('Образ не найден')
