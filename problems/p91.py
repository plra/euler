L = 50
pairs = []
for x_1 in range(L + 1):
    for x_2 in range(L + 1):
        for y_1 in range(L + 1):
            for y_2 in range(L + 1):
                pair = {(x_1, y_1), (x_2, y_2)}
                if pair in pairs:
                    continue
                # Check if PQ^2 + OQ^2 = OP^2
                pq_sq = (x_2 - x_1) ** 2 + (y_2 - y_1) ** 2
                oq_sq = x_2 ** 2 + y_2 ** 2
                op_sq = x_1 ** 2 + y_1 ** 2
                if 0 in [pq_sq, oq_sq, op_sq]:
                    continue
                if (
                    oq_sq + pq_sq == op_sq
                    or op_sq + pq_sq == oq_sq
                    or op_sq + oq_sq == pq_sq
                ):
                    # print("({}, {}), ({}, {})".format(x_1, y_1, x_2, y_2))
                    pairs.append(pair)

print(len(pairs))
