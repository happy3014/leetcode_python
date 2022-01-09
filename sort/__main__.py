import importlib
from .hill_sort import sort as hill_sort
import copy


class Num:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def __lt__(self, other):
        if not isinstance(other, Num):
            raise NotImplementedError()
        return self.value < other.value

    def __le__(self, other):
        if not isinstance(other, Num):
            raise NotImplementedError()
        return self.value <= other.value

    def __eq__(self, other):
        if not isinstance(other, Num):
            raise NotImplementedError()
        return self.value == other.value

    def __gt__(self, other):
        if not isinstance(other, Num):
            raise NotImplementedError()
        return self.value > other.value

    def __ge__(self, other):
        if not isinstance(other, Num):
            raise NotImplementedError()
        return self.value >= other.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    @classmethod
    def equal(cls, obj1, obj2):
        if not isinstance(obj1, Num) or not isinstance(obj2, Num):
            raise NotImplementedError()
        return obj1.index == obj2.index and obj1 == obj2

    @classmethod
    def int_array_2_num_array(cls, int_nums):
        return [Num(index, v) for index, v in enumerate(int_nums)]

    @classmethod
    def equal_array(cls, nums1, nums2):
        if len(nums1) != len(nums2):
            return False
        for i in range(len(nums1)):
            if not Num.equal(nums1[i], nums2[i]):
                return False
        return True

    @classmethod
    def equal_array_value(cls, nums1, nums2):
        if len(nums1) != len(nums2):
            return False
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                return False
        return True


def sort_check(init_nums, sort_func, sort_name, expected_nums):
    print(sort_name.center(40, '='))
    is_inner = False

    result_nums = sort_func(init_nums)
    if result_nums is None:
        is_inner = True
        result_nums = init_nums
    assert Num.equal_array_value(result_nums, expected_nums)
    is_stable = Num.equal_array(result_nums, expected_nums)

    print(f'是否内部排序: {"是" if is_inner else "否"}')
    print(f'是否稳定排序: {"是" if is_stable else "否"}')


if __name__ == '__main__':
    int_nums = [0, 3, 3, 1, 2, 2, 3, 5, 10]
    nums = Num.int_array_2_num_array(int_nums)
    expected_nums = sorted(nums)

    # 希尔排序
    init_nums = copy.deepcopy(nums)
    sort_check(init_nums, hill_sort, '希尔排序', expected_nums)