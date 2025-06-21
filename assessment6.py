items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories']/x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen = []

    for name, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            chosen.append(name)
            total_cost += info['cost']
            total_calories += info['calories']

    return chosen, total_cost, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)
    dp = [[0]*(budget+1) for _ in range(n+1)]

    for i in range(1, n+1):
        cost = items[names[i-1]]['cost']
        cal = items[names[i-1]]['calories']
        for w in range(budget+1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + cal)
            else:
                dp[i][w] = dp[i-1][w]

    w = budget
    chosen = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen.append(names[i-1])
            w -= items[names[i-1]]['cost']

    total_cost = sum(items[name]['cost'] for name in chosen)
    total_calories = sum(items[name]['calories'] for name in chosen)

    return chosen[::-1], total_cost, total_calories


def main():
    budget = 100
    print("Greedy Algorithm:")
    chosen_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
    print(f"Chosen items: {chosen_greedy}")
    print(f"Total cost: {total_cost_greedy}, Total calories: {total_calories_greedy}")

    print("\nDynamic Programming:")
    chosen_dp, total_cost_dp, total_calories_dp = dynamic_programming(items, budget)
    print(f"Chosen items: {chosen_dp}")
    print(f"Total cost: {total_cost_dp}, Total calories: {total_calories_dp}")


if __name__ == "__main__":
    main()
