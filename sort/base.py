class Base:
    
    """
    交换元素
    """
    def swap(self, arr, target_index, replace_index):
        tmp = arr[target_index]
        arr[target_index] = arr[replace_index]
        arr[replace_index] = tmp
