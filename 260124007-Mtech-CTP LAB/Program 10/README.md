# Program 10 — Python Project Tooling: mypy, Docker and GitHub Actions

## 1. Problem Statement
Configure mypy, Docker and GitHub Actions CI/CD for an existing Python project.

## 2. Algorithm / Concept Identification
| Item | Details |
|---|---|
| Topic | mypy + Docker + GitHub Actions |
| Static checking | mypy |
| Containerization | Docker |
| CI/CD | GitHub Actions |

## 3. Step-by-Step Example
1. Write typed Python code.
2. Run mypy to detect type errors before execution.
3. Build the project into a Docker image.
4. Run the container.
5. Configure GitHub Actions to repeat these checks automatically.

## 4. Procedure
- Type the application with Python annotations.
- Run `mypy Program_10.py`.
- Build with `docker build -t python-cpt-lab .`.
- Run with `docker run --rm python-cpt-lab`.
- In CI, install dependencies, run mypy and execute tests.

## 5. Implementation
~~~python
from typing import List


def calculate_average(values: List[float]) -> float:
    if not values:
        raise ValueError("At least one value is required")
    return sum(values) / len(values)


def main() -> None:
    values: List[float] = [10.0, 20.0, 30.0]
    print("Average:", calculate_average(values))
    print("mypy Program_10.py")
    print("docker build -t python-cpt-lab .")
    print("docker run --rm python-cpt-lab")


if __name__ == "__main__":
    main()
~~~

## 6. Input and Output
**Input:** `[10.0, 20.0, 30.0]`

**Output:** Average = `20.0`, followed by the project tooling commands.

## 7. Complexity Comparison
| Operation | Complexity |
|---|---|
| Average calculation | O(n) time |
| Memory | O(1) extra space |
| mypy | Static analysis; depends on project size |
| Docker build | Depends on project and layers |
| CI/CD | Depends on configured jobs |

## 8. Conclusion
The program demonstrates a typed Python application and the commands needed to integrate static checking, containerization and automated CI/CD.
