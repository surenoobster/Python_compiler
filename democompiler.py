def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage
text = "A man, a plan, a canal, Panama"
if is_palindrome(text):
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')

