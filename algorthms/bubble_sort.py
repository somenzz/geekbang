from __future__ import print_function


def bubble_sort(collection):
    """
    无任何优化版
    """
    compare_count=0
    length = len(collection)
    for i in range(length-1):
        print(collection)
        for j in range(length-1-i):
            compare_count+=1
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
    print(f"总循环次数{compare_count}")
    return collection


def bubble_sort2(collection):
    """
    如果没有元素交换，说明数据在排序过程中已经有序，直接退出循环
    """
    compare_count=0
    length = len(collection)
    for i in range(length-1):
        swapped = False
        print(collection)
        for j in range(length-1-i):
            compare_count+=1
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped: break  # Stop iteration if the collection is sorted.
    print(f"总循环次数{compare_count}")
    return collection

def bubble_sort3(collection):
    """
    bubble_sort2的基础上再优化。
    优化思路：在排序的过程中，数据可以从中间分为两段，一段是无序状态，另一段是有序状态。
    每一次循环的过程中，记录最后一个交换元素的公交车，它便是有序和无序状态的边界
    下一次仅循环到边界即可，从而减少循环次数，达到优化。
    """
    compare_count=0
    length = len(collection)
    last_change_index = 0 #最后一个交换的位置
    border = length-1 #有序和无序的分界线
    for i in range(length-1):
        swapped = False
        print(collection)
        
        for j in range(0,border):
            compare_count+=1
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
                last_change_index = j
        if not swapped: break  # Stop iteration if the collection is sorted.

        border = last_change_index # 最后一个交换的位置就是边界

    print(f"总循环次数{compare_count}")
    return collection



if __name__ == '__main__':
    
    print("bubble_sort begin.")
    unsorted = [3,4,2,1,5,6,7,8]
    print("bubble_sort end: ",*bubble_sort(unsorted))
    print("bubble_sort2 begin.")
    unsorted = [3,4,2,1,5,6,7,8]
    print("bubble_sort2 end:",*bubble_sort2(unsorted))
    print("bubble_sort3 begin.")
    unsorted = [3,4,2,1,5,6,7,8]
    print("bubble_sort3 end:",*bubble_sort3(unsorted))
