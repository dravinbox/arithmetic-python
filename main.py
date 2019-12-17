from sort.select_sort import SelectSort
from sort.bubble_sort import BubbleSort

print("hello,world")

arr = [3, 2, 5, 1, 4]

# 选择排序
# sort = SelectSort()
# sort.sort(arr)

# 冒泡排序
sort = BubbleSort()
sort.sort(arr)


print(arr)
