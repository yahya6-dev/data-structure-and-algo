def swap(s):
	if s == "":
		return ""
	first,second = s[:2]
	return second + first + swap(s[2:])

print(swap("abcdefgh"))
