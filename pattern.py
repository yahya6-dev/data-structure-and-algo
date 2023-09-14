def solution(pattern, source):
    d = {}
    result = 0
    for e in "qwrtyupsdfghjklmnbvcxz":
        d.update({e:1})
    for e in "aeiou":
        d.update({e:0})
    for i in range(len(source)-len(pattern)+1):
        c = source[i:i+len(pattern)]
        r = ""
        for e in c:
                k = d.get(e)
                r += str(k)
        if r == pattern:
            result += 1
    return result
print(solution("101","amazing"))
