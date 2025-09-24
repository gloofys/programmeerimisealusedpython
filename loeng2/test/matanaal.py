from sympy import symbols, Abs, solveset, S, limit, oo, diff, lambdify, FiniteSet
import numpy as np
import matplotlib.pyplot as plt

x = symbols('x', real=True)
f = Abs(2/(Abs(x) - 3) + 2)

# --- Domain ---
domain = S.Reals - FiniteSet(-3, 3)

# --- Range ---
range_str = "[0, ∞)"

# --- Roots (zeros) ---
roots = solveset(f, x, domain=S.Reals)

# --- Asymptotes ---
asymptotes = {
    "vertical": [-3, 3],
    "horizontal": 2
}

# --- Monotonicity ---
fprime = diff(f, x)
fprime_num = lambdify(x, fprime, "numpy")

intervals = [(-oo, -3), (-3, -2), (-2, 0), (0, 2), (2, 3), (3, oo)]
midpoints = [-4, -2.5, -1, 1, 2.5, 4]

increasing, decreasing = [], []
for (a, b), m in zip(intervals, midpoints):
    try:
        val = float(fprime_num(m))
    except Exception:
        continue
    if val > 0:
        increasing.append((a, b))
    elif val < 0:
        decreasing.append((a, b))

# --- Print summary ---
print("Function: f(x) = |2/(|x|-3) + 2|")
print("Domain: ", domain)
print("Range: ", range_str)
print("Zeros: ", roots)
print("Vertical asymptotes: x =", asymptotes["vertical"])
print("Horizontal asymptote: y =", asymptotes["horizontal"])
print("Increasing intervals: ", increasing)
print("Decreasing intervals: ", decreasing)

# --- Plotting ---
f_num = lambdify(x, f, "numpy")

def plot_interval(a, b, color):
    X = np.linspace(a, b, 400)
    Y = f_num(X)
    plt.plot(X, Y, color=color)

# Plot each interval separately
for a, b in increasing:
    if a == -oo: a = -10
    if b == oo: b = 10
    plot_interval(a, b, "green")

for a, b in decreasing:
    if a == -oo: a = -10
    if b == oo: b = 10
    plot_interval(a, b, "red")

# Plot asymptotes
for v in asymptotes["vertical"]:
    plt.axvline(x=v, color="black", linestyle="--", label=f"x={v}")
plt.axhline(y=asymptotes["horizontal"], color="blue", linestyle="--", label="y=2")

# Mark zeros
for r in roots:
    plt.scatter(float(r), 0, color="purple", zorder=5)

plt.ylim(-1, 10)
plt.xlim(-6, 6)
plt.title("f(x) = |2/(|x|-3)+2| with monotonicity")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
