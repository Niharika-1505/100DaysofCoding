if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(set(arr))
    l.remove(max(l))
    print(max(l))
