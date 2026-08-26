import math


def distance(coin1, coin2):
    dx = coin1[0] - coin2[0]
    dy = coin1[1] - coin2[1]
    return math.sqrt(dx * dx + dy * dy)


def closest_pair(coins):
    min_distance = float("inf")
    pair = None

    for i in range(len(coins)):
        for j in range(i + 1, len(coins)):
            current_distance = distance(coins[i], coins[j])

            if current_distance < min_distance:
                min_distance = current_distance
                pair = (coins[i], coins[j])

    return pair, min_distance


def main():
    print("\n--- CLOSEST PAIR OF COINS ---")
    print("Enter the x and y coordinates of each coin.")

    n = int(input("Enter number of coins: "))

    if n < 2:
        print("At least two coins are required.")
        return

    coins = []

    for i in range(n):
        x, y = map(
            float,
            input(f"Enter coordinates for coin {i + 1} (x y): ").split()
        )
        coins.append((x, y))

    pair, min_distance = closest_pair(coins)

    print("\n--- RESULT ---")
    print(f"Coin 1: ({pair[0][0]:g}, {pair[0][1]:g})")
    print(f"Coin 2: ({pair[1][0]:g}, {pair[1][1]:g})")
    print(f"Minimum distance: {min_distance:.2f} units")


if __name__ == "__main__":
    main()
