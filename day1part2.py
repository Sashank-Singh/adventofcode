
def word_to_digit(word):
    word_dict = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    return word_dict.get(word, word)

def find_digits(line):
    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(line[i])
        else:
            for word in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
                if line[i:].startswith(word):
                    digits.append(word_to_digit(word))
                    break
    return digits

def calculate_calibration_value(line):
    digits = find_digits(line)
    if digits:
        return int(digits[0] + digits[-1])
    return 0

def sum_calibration_values(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            total += calculate_calibration_value(line.strip())
    return total

# Read from input.txt
result = sum_calibration_values('input.txt')
print(f"The sum of all calibration values is: {result}")