from sort.base import Base


class InsertionSort(Base):

    def sort(self, arr):
        i = 0
        while i < len(arr) - 1:
            self.insert(arr, 0, i, i + 1)
            i += 1

    def insert(self, arr, start_index, end_index, target_index):
        i = end_index
        while i >= start_index:
            if arr[target_index] < arr[i]:
                self.swap(arr, target_index, i)
                target_index = i
            else:
                break
            i -= 1
