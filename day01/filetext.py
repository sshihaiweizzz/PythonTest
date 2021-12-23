filename = "digits.txt"
# names = input("enter one user name pleas:")
# name = names

# with open(filename,"a",encoding="utf-8") as file_object:
#     file_object.write(name)
# print(file_object)

while (True):
    name = input("enter one user name pleas:")
    with open(filename,'a') as file_object:
        file_object.writelines(name)
    print("welcom to pytohn")



