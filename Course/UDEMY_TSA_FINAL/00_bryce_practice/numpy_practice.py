#%%
import numpy as np

# %%
list = [1,2,3]

np_list = np.array(list)
# %%
type(np_list)
# %%
mylist = [[1,2,3],[4,5,6]]

matrix= np.array(mylist)
# %%
matrix.shape
# %%
np.arange(0,111,5)
# %%
np.ones((4,5)) +65
# %%

np.linspace(0,10,5)
# %%
np.random.rand(5,5)
# %%

# Normal distribution mean of zero sd 1
np.random.randn(10)
# %%
np.random.randint(1,100, 10)
# %%
np.random.seed(42)
np.random.rand(4)
# %%
array = np.array(5)

random_array = np.random.randint(0,50,10)
# %%
random_array
# %%
array.reshape(1)
# %%
random_array.min()
# %%
# Used to find the index of the max number
random_array.argmax()
# %%
# Used to find the index of the min number
random_array.argmin()
# %%
# Selection

arr = np.arange(0,11)

arr[8:10]
# %%
arr[1:5]
# %%
arr + 100
# %%
arr **2

# %%
# Indexing on Matrix

arr_2d = np.array([[1,2,3],[20,25,30],[35,40,45]])
# %%
arr_2d
# %%
# Select index from array
arr_2d[2][2]
# %%
arr_2d[:2,1:]
# %%
arr = np.arange(1,11)

# %%
bool_arr = arr > 4
# %%
bool_arr
# %%
arr[bool_arr]
# %%
