str = input("Enter a string: ")
if len(str) > 2 and str[:2] == 'Is':
    str = str
else:
    str1 = 'Is'
    str = str1 + str
print(str)