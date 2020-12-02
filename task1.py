def find_sum_2020_and_multiply(numbers):
    for number in numbers:
        searched_number = 2020-number
        if searched_number in numbers:
            result = number * searched_number
            return result

if __name__ == "__main__":
    lines = []
    while True:
        line = input()
        if line:
            lines.append(int(line))
        else:
            break
    print(find_sum_2020_and_multiply(lines))