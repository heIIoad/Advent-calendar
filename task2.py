import numpy as np
def find_sum_components(numbers, amount_to_find, number_to_find, start = 2, result_table = [], sum_result = 0):
    if start <= amount_to_find:
        for number in numbers:
            new_numbers = numbers[numbers.index(number)+1:]
            if (start == 2):
                result_table.append(number)
            for second_number in new_numbers:
                result_table.append(second_number)
                sum_result = sum(result_table)
                if sum_result == number_to_find:
                    if (amount_to_find == start):
                        return result_table
                    else:
                        sum_result = 0
                        continue
                elif sum_result < number_to_find and (start + 1) <= amount_to_find:
                    find_sum_components(new_numbers[new_numbers.index(second_number):], amount_to_find, number_to_find, start + 1, result_table, sum_result)
                    sum_result = sum(result_table)
                    if sum_result == number_to_find:
                        return result_table
                else:
                    sum_result = 0
                    result_table.remove(second_number)
                    continue
            result_table.remove(number)
            if start >= 3:
                break
                

if __name__ == "__main__":
    lines = []
    while True:
        line = input()
        if line:
            lines.append(int(line))
        else:
            break
    found_components = find_sum_components(lines,3,number_to_find=2020)
    print(found_components)
    print(np.prod(found_components))