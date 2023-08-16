# Program for Converting Binary to Decimal and Decimal to Binary

def type_number():
    type_num = input('Is your number binary or decimal number? ')
    return type_num.lower()

def converting_to_decimal(binary_num):
    binary_num_str = str(binary_num)
    list_of_digits = [int(i) for i in binary_num_str]
    decimal_total = 0
    for index, bit in enumerate(list_of_digits[::-1]):
        power = 2 ** index
        multiplied_digit = bit * power
        decimal_total += multiplied_digit
    return decimal_total

def converting_to_binary(decimal_num):
    binary_list = []
    if decimal_num >= 1:
        converting_to_binary(decimal_num // 2)
    binary_list.append(decimal_num % 2)
    for i in binary_list:
        print(i, end='')
        
def main():
    type_num = type_number()
    while type_num != 'quit':
        if type_num == 'binary':
            binary_num = input('Enter a binary number: ')
            while any(i not in ['0', '1'] for i in binary_num):
                binary_num = input('That number is not a binary number, enter a valid binary number: ')
            decimal_value = converting_to_decimal(int(binary_num))
            print(decimal_value)
        elif type_num == 'decimal':
            decimal_num = int(input('Enter a decimal number: '))
            converting_to_binary(decimal_num)
            print()
        else:
            type_num = input('That is not a valid binary or decimal number, enter a valid number: ')
        type_num = type_number()


main()

