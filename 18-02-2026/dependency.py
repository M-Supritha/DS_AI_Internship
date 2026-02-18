import random

# ------------------------------
# 1. Independent Event Simulation
# ------------------------------

trials = 10000
count_success = 0

for _ in range(trials):
    coin = random.choice(["Heads", "Tails"])
    die = random.randint(1, 6)
    
    if coin == "Heads" and die == 6:
        count_success += 1

print("Independent Event:")
print("Experimental Probability (Heads AND 6):", count_success / trials)
print("Theoretical Probability:", 1/12)


# ------------------------------
# 2. Dependent Event Simulation
# ------------------------------

count_red_red = 0

for _ in range(trials):
    bag = ["R"] * 5 + ["B"] * 5
    first = random.choice(bag)
    bag.remove(first)
    second = random.choice(bag)
    
    if first == "R" and second == "R":
        count_red_red += 1

print("\nDependent Event:")
print("Experimental Probability (Both Red):", count_red_red / trials)
print("Theoretical Probability:", 2/9)
