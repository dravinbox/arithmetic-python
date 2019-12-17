from sort.base import Base


class BubbleSort(Base):

    def sort(self, arr):
        i = len(arr) - 1
        while i >= 0:
            self.bubble(arr, 0, i)
            i -= 1

    def bubble(self, arr, start_index, end_index):
        i = start_index
        while i < end_index:
            if arr[i] > arr[i + 1]:
                self.swap(arr, i, i + 1)
            i += 1
