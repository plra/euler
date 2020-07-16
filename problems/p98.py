from math import sqrt, floor, ceil

words = None

with open("res/words.txt") as f:
    words = [w.replace('"', "") for w in f.readline().split(",")]

words.append("CARE")
words.append("RACE")

pairs = []
for i, w1 in enumerate(words):
    for w2 in words[i + 1 :]:
        if sorted(w1) == sorted(w2):
            pairs.append((w1, w2))

max_length = max(len(p[0]) for p in pairs)
min_length = max_length - 4
viable_pairs = [p for p in pairs if len(p[0]) >= min_length]
print("Viable pairs: ", viable_pairs)

# min_n = ceil(sqrt(10 ** (max_length - 1)))
min_n = 1
max_n = floor(sqrt(10 ** max_length - 1))
print("n in [{}, {}]".format(min_n, max_n))

sorted_strs = {n: "".join(sorted(str(n ** 2))) for n in range(min_n, max_n + 1)}
anagrams = dict()
for n, s in sorted_strs.items():
    if s in anagrams:
        anagrams[s].append(n)
    else:
        anagrams[s] = [n]


for w1, w2 in viable_pairs:
    for s, ns in anagrams.items():
        if len(s) != len(w1):
            continue
        # if len(set(s)) != len(set(w1)):
        #     continue
        for m in ns:
            for n in ns:
                if sorted(zip(w1, str(m ** 2))) == sorted(zip(w2, str(n ** 2))):
                    print(
                        "({}, {}): ({}, {}): ({}, {})".format(
                            w1, w2, m, n, m ** 2, n ** 2
                        )
                    )
