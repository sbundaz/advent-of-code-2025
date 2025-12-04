def main():
    available_fresh_id = 0
    
    with open("input.txt") as f:
        getting_fresh_id = True
        fresh_id_ranges = []

        for line in f:
            line = line.rstrip()
            
            if line == "":
                getting_fresh_id = False
            elif getting_fresh_id:
                init_range = int(line.split("-")[0])
                end_range = int(line.split("-")[1])

                fresh_id_ranges.append((init_range, end_range))
            else:
                id = int(line)

                if any(id >= range[0] and id <= range[1] for range in fresh_id_ranges):
                    available_fresh_id += 1
    
    return available_fresh_id


def main2():
    ranges = []

    with open("input.txt") as f:
        for line in f:
            line = line.rstrip()

            if line == "":
                break

            init_range = int(line.split("-")[0])
            end_range = int(line.split("-")[1])
            ranges.append([init_range, end_range])
    
    ranges.sort(key=lambda r: r[0])


    # merge overlapping ranges
    merged_ranges = [ranges[0]]

    for i in range(1, len(ranges)):
        last_range = merged_ranges[-1]
        new_range = ranges[i]

        if new_range[0] > last_range[1]:
            merged_ranges.append(new_range)
        else:
            m = [min(new_range[0], last_range[0]), max(new_range[1], last_range[1])]
            merged_ranges[-1] = m
    
    print(merged_ranges)
    fresh_ids = 0

    for r in merged_ranges:
        fresh_ids += r[1] - r[0] + 1
    
    return fresh_ids




if __name__ == "__main__":
    r = main()
    print(r)
    r = main2()
    print(r)