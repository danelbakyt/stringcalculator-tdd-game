""" Edit the function below to implement the String Calculator TDD Kata """
def add(numbers):
    if numbers == "":
        return 0
    elif "-" in number:
        return -1

    values = numbers.split(",")
    return sum(int(value) for value in values)
    
