import math
def number_length(value: int) -> int:
    # your code here
    if value == 0: 
        return 1
    return int(math.log10(abs(value))) + 1


print("Example:")
print(number_length(10))

# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")
