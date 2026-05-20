s = input("Enter the string : ")

if s[::-1] == s:
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome", s[::-1])