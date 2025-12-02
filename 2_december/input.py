def main():
    invalid_ids = []

    with open("input.txt", "r") as f:
        ranges = f.readline().rstrip().split(",")

        for r in ranges:
            init_id = int(r.split("-")[0])
            end_id = int(r.split("-")[1])

            for i in range(init_id, end_id + 1):
                if not check_valid(i):
                    invalid_ids.append(i)

    return sum(invalid_ids)


def check_valid(number):
    number_str = str(number)
    length = len(number_str)

    for i in range(1, (length // 2) + 1):
        window = number_str[0:i]
        occurrences = number_str.count(window)
        if occurrences * len(window) == length:
            return False

    return True


if __name__ == "__main__":
    r = main()
    print(r)
