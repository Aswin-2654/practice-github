def is_palindrome_loop(text):
  """
  Checks if a string is a palindrome using a while loop and two pointers.
  """
  left = 0
  right = len(text) - 1

  while left < right:
    # If characters at the two pointers don't match, it's not a palindrome
    if text[left] != text[right]:
      return False
    # Move the pointers inward
    left += 1
    right -= 1

  # If the loop completes without finding any mismatches, it is a palindrome
  return True

# Example Usage:
test_word = "racecar"
print(f"'{test_word}' is palindrome: {is_palindrome_loop(test_word)}")
