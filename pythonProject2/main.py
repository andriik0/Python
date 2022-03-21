def merge(left, right):
    merged = [0 for _ in range(len(left) + len(right))]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1

    return merged


def merge_sort(unsort_list):
    sort_list = unsort_list.copy()
    len_list = len(unsort_list)

    if len_list < 2:
        return sort_list.pop()

    co_list = []
    while True:
        if len(sort_list) == 0:
            if len(co_list) == 1:
                return co_list.pop()
            sort_list = co_list
            co_list = []

        right = sort_list.pop()
        if len(sort_list) == 0:
            co_list.append(right)
            continue
        left = sort_list.pop()
        co_list.append(merge(left, right))


def _partition(lst, start, end):
    j = start

    for i in range(start + 1, end + 1):
        if lst[i] > lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j


def _quick_sort(lst, start, end):
    if start >= end:
        return

    j = _partition(lst, start, end)
    # print(*lst)
    # print('recursive call')
    _quick_sort(lst, start, j - 1)
    # print('recursive call')
    _quick_sort(lst, j + 1, end)


def partition_(lst, start, end):
    j = start

    for i in range(start + 1, end + 1):
        if lst[i][1] < lst[start][1] or (lst[i][1] == lst[start][1] and lst[i][0] < lst[start][0]):
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]

    return j


def quick_sort_(lst, start, end):
    if start >= end:
        return

    j = partition_(lst, start, end)

    quick_sort_(lst, start, j - 1)
    quick_sort_(lst, j + 1, end)


# if __name__ == "__main__":
#     # person_count = int(input())
#     # person_list = []
#     # for _ in range(person_count):
#     #     name, age = input().split()
#     #     person_list.append((name, int(age)))
#
#     # person_list = [('john', 24), ('ann', 21), ('andrew', 24), ('nikol', 20), ]
#     person_list = [('john', 24), ('ann', 21), ('andrew', 24), ]
#     quick_sort_(person_list, 0, len(person_list) - 1)
#     print(*[item[0] for item in person_list], sep='\n')

def choose_median(lst, start, middle, end):
    mid = (start + middle + end) // 3
    if lst[mid] < lst[start]:
        lst[mid], lst[start] = lst[start], lst[mid]
    if lst[end] < lst[start]:
        lst[end], lst[start] = lst[start], lst[end]
    if lst[mid] < lst[end]:
        lst[end], lst[mid] = lst[mid], lst[end]
    return lst[end]


def partition(lst, pivot, start, end):
    print(end)
    j = start

    for i in range(start, end):
        if lst[i] <= pivot:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[end], lst[j] = lst[j], lst[end]
    return j


def quicksort(lst, start, end):
    if len(lst) < 2:
        return

    if start >= end:
        return
    middle = (start + end) // 2
    pivot = choose_median(lst, start, middle, end)
    p = partition(lst, pivot, start, end)

    quicksort(lst, start, p - 1)
    quicksort(lst, p, end)


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotindex = median(alist, first, last, (first + last) // 2)
    print(pivotindex)
    alist[first], alist[pivotindex] = alist[pivotindex], alist[first]
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and \
                alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            print(*alist)

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark


def median(a, i, j, k):
    if a[i] < a[j]:
        return i if a[k] < a[i] else k if a[k] < a[j] else j
    else:
        return j if a[k] < a[j] else k if a[k] < a[i] else i


if __name__ == '__main__':
    # lst = [*map(int, input().split())]
    lst = [*map(int, '30 60 50 20 40'.split())]

    quickSort(lst)

    # lst[0], lst[1] = lst[1], lst[0]
    # lst[-1], lst[-2] = lst[-2], lst[-1]
    # print(*lst)
