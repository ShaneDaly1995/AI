# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import codecs
import numpy as np
import datetime
# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(funct, my_list):
    # 1. We create the output variable
    res = []

    # 2. We populate the list with the higher application
    for item in my_list:
        sol = funct(item)
        res.append(sol)

    # 3. We return res
    return res

# ------------------------------------------
# FUNCTION my_filter
# ------------------------------------------
def my_filter(funct, my_list):
    # 1. We create the output variable
    res = []

    # 2. We populate the list with the higher application
    for item in my_list:
        # 2.1. If an item satisfies the function, then it passes the filter
        if funct(item) == True:
            res.append(item)

    # 3. We return res
    return res

# ------------------------------------------
# FUNCTION my_filt_func
# ------------------------------------------
def my_filt_func(item, value):

    return True if item[1] == value else False
# ------------------------------------------
# FUNCTION my_fold
# ------------------------------------------
def my_fold(funct, accum, my_list):
    # 1. We create the output variable
    res = accum

    # 2. We populate the list with the higher application
    for item in my_list:
        res = funct(res, item)

    # 3. We return res
    return res



# ------------------------------------------
# FUNCTION fold
# ------------------------------------------
def fold(tup, item, point1, point2):
    res = list(tup)
    if float(item[1]) == point1:
        res[0] = int(tup[0]) + 1
    elif float(item[1]) == point2:
        res[1] = int(tup[1]) + 1
    return tuple(res)


# ------------------------------------------
# FUNCTION my_file_reading
# ------------------------------------------
def my_file_reading(i_file_name):
    # 1. We create the output variable
    res = []

    # 2. We open the dataset file to read from it
    my_input_file = codecs.open(i_file_name, "r", encoding='utf-8')

    # 3. We parse the content of the file
    for line in my_input_file:
        # 3.1. We append the content to file_content
        res.append(line)

    # 4. We close the file
    my_input_file.close()

    # 5. We return res
    return res

# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line, coordinates):
    # We want it to return a list of elements with the following format:
    # res = (point_id, level, day, hour)
    #        integer, float, String, String)

    res = []

    (point_id, date, level, lat, long) = line.split()

    coordinates[0] = lat
    coordinates[1] = long

    res = [point_id, float(level), date]

    return res

# ------------------------------------------
# FUNCTION block1
# ------------------------------------------
def block1(dataset_dir, coordinates):
    # 1. We load the dataset into a list
    inputLIST = my_file_reading(dataset_dir)

    # 2. We count the number of measurements
    resVAL = len(inputLIST)
    # 3. We print by the screen the result computed in resVAL
    print(resVAL)

# ------------------------------------------
# FUNCTION block2
# ------------------------------------------
def block2(dataset_dir, coordinates):
    # 1. We load the dataset into a list
    inputLIST = my_file_reading(dataset_dir)

    # 2. We process each line
    # We call to my_map with process_line to find the information we want per item.
    newLIST = my_map( lambda line: process_line(line, coordinates), inputLIST )

    # 3. We filter the measurements belonging to each point
    # We call to my_filter twice, first to filter the ones with point 1 and then the ones with point 2.
    p1 = 1.74
    p2 = 0.83
    mes1 = my_filter(lambda item: my_filt_func(item, p1), newLIST)
    mes2 = my_filter(lambda item: my_filt_func(item, p2), newLIST)
    # 4. We count the number of measurements per point
    # 5. We print by the screen the result computed in resVAL
    print("{}   {}".format(len(mes1), len(mes2)))
# ------------------------------------------
# FUNCTION block3
# ------------------------------------------
def block3(dataset_dir, coordinates):
    # 1. We load the dataset into a list
    inputLIST = my_file_reading(dataset_dir)

    # 2. We process each line
    # We call to my_map with process_line to find the information we want per item.
    my_list = my_map(lambda line: process_line(line, coordinates), inputLIST)

    # 3. Operation A1: We count the measurements per point with fold
    p1 = 1.74
    p2 = 0.83
    measurement = my_fold(lambda tupple, item: fold(tupple, item, p1, p2), (0,0), my_list)
    # We call to my_fold to accumulate the results.

    # 4. We print by the screen the collection computed in resVAL
    print('Measurements at point {} = {}\nMeasurements at point {} = {}\n'.format(p1, measurement[0], p2,
                                                                                  measurement[1]))

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(dataset_dir, coordinates):
    print("Total number of measurements")
    block1(dataset_dir, coordinates)

    print("Total number of measurements per point")
    block2(dataset_dir, coordinates)

    print("Total number of measurements per point with fold")
    block3(dataset_dir, coordinates)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We provide the path to the input folder  and output folder
    dataset_file = "../my_dataset/river_lee_levels.txt"

    # 2. We add any extra variable we want to use
    coordinates = [(51.897843, -8.56668), (51.894643, -8.512962)]

    # 3. We call to our main function
    my_main(dataset_file, coordinates)
