from typing import List


def calculate_average(values: List[float]) -> float:
    if not values:
        raise ValueError("At least one value is required")
    return sum(values) / len(values)


def main() -> None:
    values: List[float] = [10.0, 20.0, 30.0]
    print("Average:", calculate_average(values))
    print("\nSuggested project commands:")
    print("mypy Program_10.py")
    print("docker build -t python-cpt-lab .")
    print("docker run --rm python-cpt-lab")


if __name__ == "__main__":
    main()
