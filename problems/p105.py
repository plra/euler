from p103 import ascending_sequences, is_special_set

if __name__ == "__main__":
    As = []
    with open("res/sets.txt") as f:
        for line in f:
            As.append([int(s) for s in line.split(",")])

    print(sum(sum(A) for A in As if is_special_set(A)))
