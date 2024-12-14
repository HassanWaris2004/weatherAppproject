from typing import List, Callable

class SortStrategy:
    def sort(self, data: List[int]) -> List[int]:
        raise NotImplementedError("This method should be overridden by subclasses.")


class QuickSort(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)


class MergeSort(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_array = []
        while left and right:
            if left[0] < right[0]:
                sorted_array.append(left.pop(0))
            else:
                sorted_array.append(right.pop(0))
        sorted_array.extend(left or right)
        return sorted_array


class SortContext:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data: List[int]) -> List[int]:
        return self._strategy.sort(data)


# Example usage
if __name__ == "__main__":
    data = [34, 7, 23, 32, 5, 62]

    # QuickSort
    quick_sort_strategy = QuickSort()
    context = SortContext(quick_sort_strategy)
    sorted_data_quick = context.sort(data)
    print("QuickSort Result:", sorted_data_quick)

    # MergeSort
    merge_sort_strategy = MergeSort()
    context.set_strategy(merge_sort_strategy)
    sorted_data_merge = context.sort(data)
    print("MergeSort Result:", sorted_data_merge)
