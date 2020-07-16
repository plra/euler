from scipy.special import binom

# 1 ball:  E = P(1) = 1
# 2 balls: E = P(1) + 2P(2) = 9/69 + 2*60/69
# 3 balls: E = P(1) + 2P(2) + 3P(3) = 9/69 * 8/68 + 2 * (1 - P(1))
# n balls: P(1) = (10 C n) / (70 C n)

# P(1 distinct) = 0
# P(<= 2 distinct) = #{20 balls in 2 bins}/#{20 balls} = 20c20 * 7c2 / 70c20
# P(<= 3 distinct) = #{20 balls in 3 or fewer bins}/70c20 = 30c20 * 7c3 /70c20
# P(k distinct) = (1 - P(k-1 distinct - ... - P(1 distinct))) * P(next in new bucket)

n_colors = 5
balls_per_color = 5
n_picks = 5
n_balls = n_colors * balls_per_color

p_at_most_k_distinct = {1: 0}
for k in range(2, n_colors + 1):
    p = binom(balls_per_color*k, n_picks) * \
        binom(n_colors, k) / binom(n_balls, n_picks)
    p_at_most_k_distinct[k] = p

E = 0
for k in range(2, n_colors + 1):
    p_k_distinct = p_at_most_k_distinct[k] - p_at_most_k_distinct[k-1]
    E += k * p_k_distinct
    print(k, p_k_distinct)

print('{:.10f}'.format(E))
