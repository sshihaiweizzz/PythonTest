from selenium import webdriver
# wd = webdriver.Chrome()
# wd.get("http://10.10.11.49/Modules/Start/start.aspx#")
# pass
# def func1(num1,num2):
#     print(num1**3 +num2**3)
#
# s = func1(23,34)
# print(s)

def study_name(name,age=45):
    print("他的名字是:",name +"\n年龄是:",age)

# study_name("张飞")
# s = input("请输入数字:")
# a = int(s)
# n = a *75/100
# w = str(n)
# print("sad"+w)

# def lens():
#     s = input("请输入一段数字:")
#     return s
# print(len(lens()))
# var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
# var1[1] = "Oh my God"
# var1[2] = "2323"
# print(var1)

# heght = input("请输入身高:")
# heghts = int(heght)
# print(type(heghts))
# weight = input("请输入体重")
# weights = int(weight)
# age = input("请输入年龄")
# ages = int(age)
#
# if ages < 10:
#     print("年龄太小")
# elif ages< 60 and ages >=10:
#     bmi = weights/(heghts**2)
#     if bmi > 24:
#         print("太重了")
#     elif bmi<18 :
#         print("太轻了")
#     else:
#         print("刚刚好")
# else:
#     print("年龄太大")

str = "123 123 123 123 123"
str1 = str.split(" ")
print(str.replace('123','999'))
print(str.startswith("123"))
print(str.endswith("123"))
str1.remove("123")
print(str1)


