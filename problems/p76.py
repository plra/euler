def count_partitions(n, max_int, lookup):
    max_int = min(n, max_int)
    if max_int <= 1:
        lookup[(n, max_int)] = 1
        val = 1
    elif (n, max_int) in lookup:
        val = lookup[(n, max_int)]
    else:
        k = 0
        for first in range(max_int, 0, -1):
            subpartitions, _ = count_partitions(n - first, first, lookup)
            k += subpartitions
        val = k
    lookup[(n, max_int)] = val
    return val, lookup

for n in range(101):
    print(n, count_partitions(n, n-1, {})[0])