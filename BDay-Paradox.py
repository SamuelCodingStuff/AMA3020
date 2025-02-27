import matplotlib.pyplot as plt

# Returning the probability that two people will have the same birthday
# Assumes no leap years and an even distribution of birthdays
def birthday_problem_probability(n: int) -> float:
    if n > 365:  
        return 1.0
    
    prob = 1.0
    for i in range(n):
        prob *= (365 - i) / 365.0
    
    return 1 - prob

max_n = 100
x_values = range(1, max_n + 1)
y_values = [birthday_problem_probability(n) for n in x_values]

plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, linestyle='-', color='b', label="Probability Curve")

# Marking y = 0.5
plt.axhline(0.5, color='gray', linestyle='--', alpha=0.7, label="50% Probability")

# Marking x = 23
n_23 = 23
p_23 = birthday_problem_probability(n_23)

# Vertical line at x = 23
plt.axvline(n_23, color='red', linestyle='--', alpha=0.7, label="n = 23")

plt.scatter(n_23, p_23, color='red', zorder=5)
plt.text(n_23+1, p_23, f"{p_23:.1%}", color='red', va='center', fontsize=10)

plt.title("Birthday Problem: Probability of at Least One Shared Birthday")
plt.xlabel("Number of People (n)")
plt.ylabel("Probability")
plt.grid(True)
plt.legend(loc="best")

plt.show()
