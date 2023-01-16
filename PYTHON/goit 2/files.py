
# new_file = open('text2.txt', 'w')
file = open("text.txt", 'r')
text = file.read()
# print(file.read()) # покажет файл
# print(text.split())
with open('text.txt', 'r') as file:
    print(file.read())
    # file.read()

# name = open('nameof file to create.rtf', 'w') # how to create file with python


# name = open('name of file to look to console', 'r' ) # how to read file in console
# print(name.read()) # how to read file in console

# w
# r
