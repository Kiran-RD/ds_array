def reverse(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    return arr


def main():
    arr = list(map(int, input().split()))
    print(reverse(arr))


if __name__ == '__main__':
    main()