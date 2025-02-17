def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))

def number_with_max_digit_sum(numbers):
    return max(numbers, key=sum_of_digits)
###########main program##########3


number = int(input())
lst_number = []
for i in range(1, number + 1):
    lst_number.append(i)

result = number_with_max_digit_sum(lst_number)
print(result)

