# Python3 program to rotate an array by d elements
# Function to left rotate arr[] of size n by d

def left_rotate_approach_1(arr, d):
    # Removing d%n number of elements from left side of the list
    # and placing then on the right of the list
    n = len(arr)
    d = d % n
    return arr[d:] + arr[:d]


def left_rotate_approach_2(arr, d):
    # Running a for loop d%n number of times and in every iteration
    # the left most element is moved to rightmost position and
    # every element is shifted to left by 1
    n = len(arr)
    d = d % n
    for _ in range(d):
        temp = arr[0]
        for i in range(1, n):
            arr[i-1] = arr[i]
        arr[-1] = temp
    return arr


def main():
    arr = list(map(int, input().split()))
    d = int(input())
    print(left_rotate_approach_1(arr, d))
    print(left_rotate_approach_2(arr, d))


if __name__ == '__main__':
    main()

# Test data
# Input ------------------------
# 1 2 3 4 5 6 7
# 17
# Output ------------------------
# [4, 5, 6, 7, 1, 2, 3]
# [4, 5, 6, 7, 1, 2, 3]
