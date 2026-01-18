from core import strength_evaluate

print("Password Strength Checker\n")

password = input("Enter password to evaluate: ")

result = strength_evaluate(password)

print("\n--- Strength Report ---")
print("length:", result["length"])
print("has_upper:", result["has_upper"])
print("has_lower:", result["has_lower"])
print("specialcharacter:", result["specialcharacter"])
print("repeats:", result["repeats"])
print("sequence:", result["sequence"])
print("rating:", result["rating"])
