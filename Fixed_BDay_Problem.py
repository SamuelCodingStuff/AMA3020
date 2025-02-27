import matplotlib.pyplot as plt
import math

def fixed_birthday_probability(n: int) -> float:
    none_prob = (364/365)**n  
    return 1 - none_prob      

max_n = 365
x_values = range(1, max_n + 1)
y_values = [fixed_birthday_probability(n) for n in x_values]

# 1 - (364/365)^n = 0.5  => (364/365)^n = 0.5
# => n * ln(364/365) = ln(0.5)  => n = ln(0.5) / ln(364/365)
n_50_exact = math.log(0.5) / math.log(364/365)
n_50 = int(round(n_50_exact))
p_50 = fixed_birthday_probability(n_50)

plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, linestyle='-', color='blue', label="Probability Curve")
plt.axhline(0.5, color='gray', linestyle='--', alpha=0.7, label="50% Probability")
plt.axvline(n_50, color='red', linestyle='--', alpha=0.7, label=f"n ≈ {n_50}")
plt.scatter(n_50, p_50, color='red', zorder=5) 
plt.text(n_50 + 2, p_50, f"{p_50:.1%}", color='red', va='center', fontsize=10)

plt.title("Fixed Birthday Problem: Probability at Least One Person Has a Specific Birthday")
plt.xlabel("Number of People (n)")
plt.ylabel("Probability")
plt.grid(True)
plt.legend(loc="best")

plt.show()
