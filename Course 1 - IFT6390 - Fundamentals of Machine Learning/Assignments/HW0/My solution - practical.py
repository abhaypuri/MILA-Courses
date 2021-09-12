import numpy as np
def make_array_from_list(some_list):
     print(some_list, type(some_list))
     some_list = np.array(some_list)
     print(some_list, type(some_list))
     return some_list

def make_array_from_number(num):
    print(num, type(num))
    new_num = np.array([num])
    print(new_num, len(new_num))
    return new_num

class NumpyBasics:
    def add_arrays(self, a, b):
        return np.add(a,b)

    def add_array_number(self, a, num):
        return np.add(a,num)

    def multiply_elementwise_arrays(self, a, b):
        return np.multiply(a,b)

    def dot_product_arrays(self, a, b):
        return np.dot(a,b)

    def dot_1d_array_2d_array(self, a, m):
        # consider the 2d array to be like a matrix
        return np.dot(a,m)
