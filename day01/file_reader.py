filename = 'digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.rstrip()
print(pi_string[:20]+"...")
print(len(pi_string))

birthday  = input("Enter your birthday,in th form mmddyy:")
if birthday in pi_string:
    print("You birthday appears in the first million digits of pi !")
else:
    print("You birthday does not appear in the first million digits of pi !")








# for line in lines:
#     print(line.rstrip())
#
#     # for line in file_object:
#         # print(line.rstrip())
#     # contens = file_object.read()
#     # print(contens.rstrip())