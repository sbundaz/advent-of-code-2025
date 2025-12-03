def main():
    result = 0
    with open("input.txt", "r") as f:
        for line in f:
            result += calculate_joltage(line.rstrip())

    return result


def calculate_joltage(number: str):
    k = 12
    digit_to_remove = len(number) - k
    stack = []

    for current_digit in number:
        while stack and digit_to_remove > 0 and stack[-1] < current_digit:
            stack.pop()
            digit_to_remove -= 1
        stack.append(current_digit)
    
    result = stack[:k]
    return int(''.join(result))


if __name__ == "__main__":
    r = main()
    print(r)
