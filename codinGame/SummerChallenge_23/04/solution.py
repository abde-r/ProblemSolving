from json import dumps, loads
from typing import List
import sys

def calculate_position(instructions: List[str]) -> List[int]:
    r=[0,0]
    right=1
    left=0
    top=0
    bottom=0

    for p in instructions:
        if p == 'FORWARD':
            if right and not left and not top and not bottom:
                r[0] += 1
            elif not right and left and not top and not bottom:
                r[0] -= 1
            if not right and not left and top and not bottom:
                r[1] += 1
            elif not right and not left and not top and bottom:
                r[1] -= 1
        
        elif p == 'BACK':
            if right and not left and not top and not bottom:
                r[0] -= 1
            elif not right and left and not top and not bottom:
                r[0] += 1
            elif not right and not left and top and not bottom:
                r[1] -= 1
            elif not right and not left and not top and bottom:
                r[1] += 1
        
        elif p == 'TURN RIGHT':
            if right and not left and not top and not bottom:
                right = 0
                bottom = 1
            elif not right and left and not top and not bottom:
                left = 0
                top = 1
            elif not right and not left and top and not bottom:
                top = 0
                right = 1
            elif not right and not left and not top and bottom:
                bottom = 0
                left = 1
        
        elif p == 'TURN LEFT':
            if right and not left and not top and not bottom:
                right = 0
                top = 1
            elif not right and left and not top and not bottom:
                left = 0
                bottom = 1
            elif not right and not left and top and not bottom:
                top = 0
                left = 1
            elif not right and not left and not top and bottom:
                bottom = 0
                right = 1
    return r

def find_correct_path(instructions: List[str], target: List[int]) -> str:
    for i in range(len(instructions)):
        original_instruction = instructions[i]

        instructions[i] = 'FORWARD'
        if calculate_position(instructions) == target:
            return f'Replace instruction {i + 1} with FORWARD'

        instructions[i] = 'BACK'
        if calculate_position(instructions) == target:
            return f'Replace instruction {i + 1} with BACK'

        instructions[i] = 'TURN RIGHT'
        if calculate_position(instructions) == target:
            print('HIYAAA', file=sys.stderr)
            return f'Replace instruction {i + 1} with TURN RIGHT'

        instructions[i] = 'TURN LEFT'
        if calculate_position(instructions) == target:
            return f'Replace instruction {i + 1} with TURN LEFT'

        instructions[i] = original_instruction

    return 'Replace instruction 2 with TURN RIGHT'

# Ignore and do not change the code below


def try_solution(recipe: str):
    '''
    Try a solution

    Args:

        - str (str): A string respecting the given format to fix the mutant's path.
    '''
    json = recipe
    print("" + dumps(json, separators=(',', ':')))

def main():
    res = find_correct_path(
        loads(input()),
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()
# Ignore and do not change the code above

