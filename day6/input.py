def main():
    numbers = []
    signs = []

    with open("input.txt") as f:

        for line in f:
            line = line.strip().split()

            if line[0] == "*" or line[0] == "+":
                signs = line
            else:
                numbers.append([int(l) for l in line])

        print(numbers)

    result = 0

    for i in range(len(signs)):
        if signs[i] == "+":
            col_result = 0
            
            for line in numbers:
                col_result += line[i]
        else:
            col_result = 1

            for line in numbers:
                col_result *= line[i]
        
        result += col_result
    
    return result






if __name__ == "__main__":
    r = main()
    print(r)
