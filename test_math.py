def calculate_sum(a: int, b: int) -> int:
    # TODO: Add input validation
    return a + b

def multiply_numbers(x: int, y: int) -> int:
    result = x * y  # This could overflow for large numbers
    return result

# Example usage with potential security issues
user_input = input("Enter a number: ")
result = calculate_sum(int(user_input), 10)
