def checkio(words: str) -> bool:
    # add your code here
    diviser_words = words.split()
    counter = 0
    for diviser_word in diviser_words:
        if diviser_word.isalpha():
            counter = counter + 1
            if counter == 3:
                return True 
        if diviser_word.isdigit():
            counter = 0
    return False


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
