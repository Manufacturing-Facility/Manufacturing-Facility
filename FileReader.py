from decimal import Decimal
from random import randrange

"""
The file to read from dat files and store those data into program
"""


# read data from file and return the content as a double list
def read_from_file(file_name):
    time_data = []
    file = open("data/" + file_name, 'r')
    while 1:
        line = file.readline()
        if line.rstrip() == '':
            break
        time_data.append(Decimal(line.rstrip()))
    return time_data


# get a data in the random place of the argument data_array
def get_random_data(data_array):
    index = randrange(len(data_array))
    return data_array[index]


# read data from dat file, concrete data lists
insp1 = read_from_file("servinsp1.dat")
insp22 = read_from_file("servinsp22.dat")
insp23 = read_from_file("servinsp23.dat")
ws1 = read_from_file("ws1.dat")
ws2 = read_from_file("ws2.dat")
ws3 = read_from_file("ws3.dat")
