# Function to implement Stirling Number of the Second Kind
def stirling_second_kind(n, k):
    if k > n: 
        return 0
    if n == 0 and k == 0: 
        return 1
    if k == 0 or n == 0: 
        return 0
    # Recurrence: S(n, k) = k * S(n-1, k) + S(n-1, k-1)
    return k * stirling_second_kind(n-1, k) + stirling_second_kind(n-1, k-1)

# The below function is equivalent to:
# P(A'') = \left(\frac{1}{d^{m+n}}\right)\sum^m_{i=0} \sum^n_{j=0}S_2(m,i)S_2(n,j)\prod^{i+j-1}_{k=0}d-k
def no_birthday_collision_probability(m, n, d=365):
    total_ways = d**(m+n) # Implementing for 1/d^(m+n), this is the basic 
    count_no_collisions = 0
    for i in range(m+1):
        S2_m_i = stirling_second_kind(m, i)
        for j in range(n+1):
            S2_n_j = stirling_second_kind(n, j)
            # Choose i+j distinct days out of d = d*(d-1)*...*(d - (i+j) + 1)
            r = i + j
            if r > d:
                # If i+j > d, the product is effectively 0
                continue
            ways_distinct_days = 1
            for k in range(r):
                ways_distinct_days *= (d - k)
            count_no_collisions += S2_m_i * S2_n_j * ways_distinct_days
    return count_no_collisions / total_ways # This is the entire equation over the d^(m+n) part

d = 365
threshold = 0.5
max_people = 60

def find_threshold(d=365, threshold=0.5, max_people=60):
    for m in range(1, max_people//2 + 1):
        p0 = 1 - no_birthday_collision_probability(m, m, d=d)
        print("Number of People Equally Split: ", 2*m, "- Probability: ", p0)
        if p0 >= threshold:
            return (2*m, p0)
    return None

group_size, prob_none = find_threshold(threshold=0.5)
print(f"Minimum Total = {group_size} people")
print(f"Probability of Collision = {prob_none:.4f}")
