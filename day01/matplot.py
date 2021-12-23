import matplotlib.pyplot as plt
# import PySimpleGUI as sg
# import time
# mylist = [1,2,3,4,5,6,7,8]
# for i, item in enumerate(mylist):
#     sg.one_line_progress_meter('This is my progress meter!', i+1, len(mylist), '-key-')
#     time.sleep(1)
from alive_progress import  alive_bar
import time
with alive_bar(100) as bar:
    for item in range(100):
        time.sleep(.10)
        bar()


# squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 110]
# input_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# plt.plot(input_value, squares, linewidth=2)
# plt.scatter(3,2,s= 100,color= "red")
# plt.xlabel("x value", fontsize=12)
# plt.ylabel("y value", fontsize=12)
# plt.title("Matplotlib", fontsize=18)
# plt.tick_params(axis="both",which='major', labelsize=10)
# plt.show()
