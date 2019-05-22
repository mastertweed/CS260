import math
import numpy as np
import matplotlib.pyplot as plt
import LinearAlgebra

# All the files names in a list
data_files = ['ECE203Data1.txt', 'ECE203Data2.txt', 'ECE203Data3.txt', 'ECE203Data4.txt',
              'ECE203Data5.txt', 'ECE203Data6.txt', 'ECE203Data7.txt']


# Function to open, then read and split the txt tile into a list
def open_split(file):
    data = open(file, 'r')
    data_read = data.read().split()
    return data_read


# Convert all values in a list into float values
def convert_float(ls):
    for i in range(len(ls)):
        ls[i] = float(ls[i])
    return ls


# Convert list of tuples to x and y lists
def x_y(ls):
    x_list = []
    y_list = []

    for i in range(int(len(ls)/2)):
        x_list.append(ls[2*i])
        y_list.append(ls[2*i+1])

    xy_list = [x_list, y_list]

    return xy_list

# Create all the lists of data
data1_ls = open_split(data_files[0])
data2_ls = open_split(data_files[1])
data3_ls = open_split(data_files[2])
data4_ls = open_split(data_files[3])
data5_ls = open_split(data_files[4])
data6_ls = open_split(data_files[5])
data7_ls = open_split(data_files[6])

data_all = [data1_ls, data2_ls, data3_ls, data4_ls, data5_ls, data6_ls, data7_ls]

# Delete all the Non numerical values in the lists
del data_all[0][0:2]
del data_all[1][0:2]
del data_all[2][0:2]
del data_all[3][0:2]
del data_all[4][0:4]
del data_all[5][0:5]
del data_all[6][0:5]

# Loop through list of all data lists, convert to float, convert to x and y, then print
for i in range(len(data_all)):
    convert_float(data_all[i])
    data_all[i] = x_y(data_all[i])
    # print(data_all[i])

# ---------------------


# Linear regression model
def linearmodel(data):

    # Values needed for calculation: xy, sum(xy), x^2, sum(x^2)
    xy = len(data[0]) * sum([data[0][i] * data[1][i] for i in range(len(data[0]))])
    sum_xy = sum(data[0]) + sum(data[1])
    x_pow2 = len(data[0]) * sum([data[0][i]**2 for i in range(len(data[0]))])
    xsum_pow2 = sum(data[0])**2

    # Linear fit A1 value
    B = (xy - sum_xy)/(x_pow2 - xsum_pow2)

    # Linear fit A0 value
    a = sum(data[1])/len(data[1]) - B*(sum(data[0])/len(data[0]))

    return a, B


# Exponential regression model
def expo(data):

    # Values need for calculation: log(y), n, x^2, xlog(y), sum(x)
    log_y = sum([math.log(i) for i in data[1]])
    n = len(data[0])
    x_pow2 = sum([i**2 for i in data[0]])
    xlog_y = sum([data[0][i] * math.log(data[1][i]) for i in range(len(data[0]))])
    x_sum = sum(data[0])

    num_a = (log_y * x_pow2) - (x_sum * xlog_y)
    den_a = (n * x_pow2) - (x_sum**2)

    num_b = (n * xlog_y) - (x_sum * log_y)
    dem_b = (n * x_pow2) - (x_sum**2)

    # Exponential fit a value
    a = num_a / den_a

    # Exponential fit b value
    b = num_b / dem_b

    return a, b


# Saturation regression model
def saturation(data):

    # Values needed for Calculation
    n = len(data[0])
    x1 = sum([1/i for i in data[0]])
    y1 = sum([1/i for i in data[1]])
    xy = sum([1/(data[0][i] * data[1][i]) for i in range(len(data[0]))])
    x_pow2 = sum([1/(i**2) for i in data[0]])

    # Linear fit a value
    a = (((1/n) * y1 * x_pow2) - ((1/n) * x1 * xy)) / (x_pow2 - ((1/n) * (x1**2)))

    # Linear fit b value
    b = ((xy) - ((1/n) * x1 * y1)) / (x_pow2 - ((1/n) * (x1**2)))

    return a, b

# --------------------


# Function containing all regression types excluding polynomial
def regression(file, type):
    setting = type

    # Linear fit
    if setting == 1:

        a, B = linearmodel(file)

        # New y values appended to original list
        new_y = [a + (B * point) for point in file[0]]
        file.append(new_y)

        # Title
        title = 'y = %.3f + %.3fx  ' % (a, B)

        # Plot the original values and the adjusted values
        plt.plot(file[0], file[1], 'bo', file[0], file[2], '--r')
        plt.title(title)
        plt.show()

    # Exponential Fit
    elif setting == 2:

        a, b = expo(file)
        A = math.exp(a)

        # New y values appended to original list
        new_y = [(A * (math.exp(b * point))) for point in file[0]]
        file.append(new_y)

        # Title
        title = 'y = %.3f * e(%.3fx)  ' % (A, b)

        # Plot the original values and the adjusted values
        plt.plot(file[0], file[1], 'bo', file[0], file[2], '--r')
        plt.title(title)
        plt.show()

    # Power Fit
    elif setting == 3:

        a, b = linearmodel(file)
        A = math.exp(a)

        new_y = [A * (b ** point) for point in file[0]]
        file.append(new_y)

        # Title
        title = 'y = %.3fx^%.3f  ' % (A, b)

        # Plot the original values and the adjusted values
        plt.plot(file[0], file[1], 'bo', file[0], file[2], '--r')
        plt.title(title)
        plt.show()

    # Saturation Fit
    elif setting == 4:

        a1, b1 = saturation(file)

        a = 1/a1
        b = a1*a

        new_y = [a * (point/(point + b)) for point in file[0]]
        file.append(new_y)

        # Title
        title = 'y = %.3fx / (%.3f + x)  ' % (a, b)

        # Plot the original values and the adjusted values
        plt.plot(file[0], file[1], 'bo', file[0], file[2], '--r')
        plt.title(title)
        plt.show()


# Polynomial Regression
# def polynomial(file, degree):
#
#         mat = []
#         for value in file[0]:
#             ls = [1]
#             for d in range(1, degree+1):
#                 ls.append(round(value**d, 6))
#             mat.append(ls)
#
#         matrix = np.array(mat)
#         yvec = np.array(file[1])
#
#         mat_1 = LinearAlgebra.transpose(matrix)
#         mat_2 = LinearAlgebra.mat_mult(mat_1, matrix)
#         mat_3 = LinearAlgebra.inverse(mat_2)
#         mat_4 = (LinearAlgebra.mat_mult(mat_1, yvec))
#         final = list(LinearAlgebra.mat_mult(mat_3, mat_4))
#
#         # invertmat = LinearAlgebra.inverse(LinearAlgebra.mat_mult(LinearAlgebra.transpose(matrix), matrix))
#         # coefmat = (LinearAlgebra.mat_mult(LinearAlgebra.transpose(matrix), yvec))
#         # final = list(LinearAlgebra.mat_mult(invertmat, coefmat))
#
#         np.linalg.inv()
#
#         new_y = [sum([final[i] * (point ** i) for i in range(len(final))]) for point in file[0]]
#
#         # Title
#         title = 'y = '
#         for i in range(len(final)):
#             title = title + str(round(final[i], 2)) + 'x' + '^' + str(i)
#             if i != len(final)-1:
#                 title = title + ' + '
#
#         # Plot the original values and the adjusted values
#         plt.plot(file[0], file[1], 'bo', file[0], new_y, '--r')
#         plt.title(title)
#         plt.show()


regression(data_all[0], 1)
regression(data_all[1], 1)
regression(data_all[2], 2)
regression(data_all[3], 3)
regression(data_all[4], 4)
# polynomial(data_all[5], 3)
# polynomial(data_all[6], 10)
