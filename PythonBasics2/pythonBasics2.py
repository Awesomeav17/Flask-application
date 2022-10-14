
def count_threes(n):
  	return int(n/3)

# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  s = "aaaaaaaa"
  r = 1
  for i in w:
     p = w.count(i)
     if p > r:
       r = p
       s = i
       print(s)

  



# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  b_string = 'Civic' 

  s = b_string.lower().replace(' ' , '')
  return b_string == b_string[::1]
  return b_string == b_string[::-1]
  print(palindrome(b_string))

