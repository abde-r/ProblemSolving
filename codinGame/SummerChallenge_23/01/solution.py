from json import dumps, loads
from typing import List


def best_remaining_mutant(mutant_scores: dict, threshold: int) -> str:
    remaining_mutants = {key: value for key, value in mutant_scores.items() if value < threshold}
    best_mutant = max(remaining_mutants, key=lambda x: remaining_mutants[x])

    return best_mutant

# Ignore and do not change the code below


def try_solution(output: str):
    json = output
    print("" + dumps(json, separators=(',', ':')))

def main():
    res = best_remaining_mutant(
        loads(input()),
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()
# Ignore and do not change the code above

