def is_palindrome_slicing(text):
  """
  Checks if a string (or number converted to string) is a palindrome using slicing.
  """
  # Comparing the string with its reversed version
  return text == text[::-1]

# Example Usage:
word = "madam"
number = 121
sentence = "A man, a plan, a canal, Panama"

print(f"'{word}' is palindrome: {is_palindrome_slicing(word)}")
print(f"'{number}' is palindrome: {is_palindrome_slicing(str(number))}")

def clean_and_check(sentence):
    cleaned_text = ''.join(char.lower() for char in sentence if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

print(f"'{sentence}' is palindrome  (cleaned): this is easy code compsare to the next code that you know right or not  {clean_and_check(sentence)}")
