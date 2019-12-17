from sort.base import Base


class SelectSort(Base):

    def minIndex(self, arr, start_index, end_index):
        min_index = start_index
        for i in range(start_index, end_index):
            if arr[i] < arr[min_index]:
                min_index = i
        return min_index

    def sort(self, arr):
        for i in range(0, len(arr)):
            min_index = self.minIndex(arr, i, len(arr))
            if min_index != i:
                self.swap(arr, i, min_index)
