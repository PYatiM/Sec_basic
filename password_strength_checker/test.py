from core import strength_evaluate

test_cases = [
    "abc123",
    "Password",
    "Pass1234",
    "P@ssw0rd",
    "StrongP@ss123!",
    "ABCDEF123456",
    "aB3!xY9@Lm"
]

print("Password Strength Test Suite\n")

for i, pwd in enumerate(test_cases, 1):
    result = strength_evaluate(pwd)

    print(f"Test Case {i}")
    print("Password:", pwd)
    print("Result:", result)
    print("-" * 40)
