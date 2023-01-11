#!/usr/bin/python3

def weight_average(my_list=[]):
    weight_sum = [x[0] * x[1] for x in my_list]
    weight_sum = sum(weight_sum)

    sum = 0
    for i in my_list:
        sum += i[0]

    return weight_sum / sum
