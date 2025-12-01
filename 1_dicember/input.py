def main():
    zeros = 0
    current_pos = 50

    with open("input.txt", "r") as f:
        for line in f:
            direction = line.rstrip()[0]
            rotation = int(line.rstrip()[1:])
            zeros += rotation // 100
            remaining_rotation = rotation % 100

            if direction == "R":
                current_pos += remaining_rotation

                if current_pos > 100:
                    zeros += 1

                current_pos %= 100

                if current_pos == 0:
                    zeros += 1
            elif direction == "L":
                init_pos = current_pos
                current_pos -= remaining_rotation

                if current_pos == 0:
                    zeros += 1
                elif init_pos > 0 and current_pos < 0:
                    zeros += 1

                current_pos %= 100
            else:
                raise Exception()

    return zeros


if __name__ == "__main__":
    r = main()
    print(r)
