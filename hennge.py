def calculate_sum_of_squares_recursive(numbers, index, sum_of_squares):
    if index == len(numbers):
        return sum_of_squares
    number = numbers[index]
    if number > 0:
        sum_of_squares += number * number
    return calculate_sum_of_squares_recursive(numbers, index + 1, sum_of_squares)

def process_test_cases_recursive(num_test_cases, current_test_case, total_sum):
    if current_test_case == num_test_cases:
        return total_sum
    num_integers = int(input())
    numbers = list(map(int, input().split()))
    sum_of_squares = calculate_sum_of_squares_recursive(numbers, 0, 0)
    total_sum.append(sum_of_squares)
    return process_test_cases_recursive(num_test_cases, current_test_case + 1, total_sum)

def check_stack(stack):
    if stack:
        d=stack.pop(0)
        print(d)
        return check_stack(stack)

def main():
    num_test_cases = int(input())
    total_sum = process_test_cases_recursive(num_test_cases, 0, [])
    check_stack(total_sum)

if __name__ == "__main__":
    main()