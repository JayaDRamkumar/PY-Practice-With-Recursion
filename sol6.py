# 6. recursive_reverse — Uses recursion to reverse a string.
def recursive_reverse(str, i=0):
  #empty string case
  if len(str)==0:
    return ""
  #base case
  elif i == len(str)-1:
    return str[0]
  else:
    #recursive case
    return str[-1-i] + recursive_reverse(str, i+1)

print(recursive_reverse("aaaa"))
print(recursive_reverse("aaba"))
print(recursive_reverse("apple"))
print(recursive_reverse(""))
  