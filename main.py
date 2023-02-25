# DATA TYPES IN NUMPY ARRAYS
import numpy as np
var = np.array([1,2,3,4])
print("Data Type  :",var.dtype)


var = np.array([1,2,3,4,3434,3434j])
print("Data Type  :",var.dtype)

var = np.array([1,2.0,3,4.9])
print("Data Type  :",var.dtype)

var = np.array(["a","b","c"])
print("Data Type  :",var.dtype)

var = np.array([1,2,3j])
print("Data Type: ",var.dtype)

var = np.array([1,2,3j,1,"c","d",4])
print("Data Type: ",var.dtype)


# TO change one data type into another
x = np.array([1,2,3,4])
print("data Type ;" , x.dtype)

#changing into int8

x = np.array([1,2,3,4],dtype = np.int8)
print("data Type ;" , x.dtype)

x = np.array([1,2,3,4],dtype = "f")
print("data Type ;" , x.dtype)




x3 = np.array([1,2,3,4])
new = np.float32(x3)
new_one = np.int_(new)


print(x3)
print(new)
print(new_one)
print("Data Type :" , x3.dtype)
print("Data Type :", new.dtype)
print("Data Type : ",new_one.dtype)

