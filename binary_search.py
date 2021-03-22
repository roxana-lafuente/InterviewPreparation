def binary_search(l, r, xs, value):
    while l <= r:
        m = ( l + r ) // 2
        if xs[m] == value:
            return m
        elif xs[m] > value:
            r = m - 1
        else: # xs[m] < value
            l = m + 1
    return -1


D = 10
xs = list(range(1, D+1))
print("List: ", xs)
for value in [-1, 1, 3, 5, 7, 9, 10, 11, 23]:
    print("Looking for: ", value)
    i = binary_search(0, D-1, xs, value)
    if i == -1:
        print("We could not find element %s" % value)
    else:
        print("We found the element at position %s" % i)
    print("\n")