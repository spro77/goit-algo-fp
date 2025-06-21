import random
import matplotlib.pyplot as plt

N = 100_000

sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(N):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    s = die1 + die2
    sum_counts[s] += 1

sum_probs = {s: count / N for s, count in sum_counts.items()}

analytical_probs = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

print(f"{'Sum':>3} | {'Monte Carlo':>12} | {'Analytical':>12}")
print('-'*36)
for s in range(2, 13):
    print(f"{s:>3} | {sum_probs[s]*100:10.2f}% | {analytical_probs[s]*100:10.2f}%")

plt.figure(figsize=(10,6))
plt.bar(sum_probs.keys(), [v*100 for v in sum_probs.values()], alpha=0.6, label='Monte Carlo')
plt.plot(list(analytical_probs.keys()), [v*100 for v in analytical_probs.values()], 'ro-', label='Analytical')
plt.xlabel('Sum of two dice')
plt.ylabel('Probability (%)')
plt.title('Probability Distribution of Dice Sums (Monte Carlo vs Analytical)')
plt.legend()
plt.grid(True)
plt.show()
