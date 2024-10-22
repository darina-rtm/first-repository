def is_palindrome(text):
  text = text.lower().replace(" ", "")
  return text == text[::-1]
text = input("Введите любой текст: ")
if is_palindrome(text):
  print("Это палинддддддддддддром!")
else:
  print("Это не палиндром.")
