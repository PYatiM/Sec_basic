import math

pool = {
    "L": "abcdefghijklmnopqrstuvwxyz",
    "U": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "S": "!@#$%^&*()}{[]<>/?\\|;:=~",
    "D": "1234567890"
}

pool_size = sum(len(v) for v in pool.values())


class MyRandom:
    def __init__(self, seed=123456):
        self.seed = seed
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def random(self):
        return self.next() / self.m

    def pick_char(self, text):
        if not text:
            return None
        index = int(self.random() * len(text))
        return text[index]

    def num(self, num1, num2):
        if num1 == 0 or num2 == 0:
            return 0
        val = int((self.random() * ((num1 * num2) % (num2 // num1 + 1))) % 10)
        return val


def charcheck(password):
    passs = {"L": 0, "D": 0, "U": 0, "S": 0}

    for ch in password:
        if ch in pool["L"]:
            passs["L"] += 1
        elif ch in pool["D"]:
            passs["D"] += 1
        elif ch in pool["U"]:
            passs["U"] += 1
        elif ch in pool["S"]:
            passs["S"] += 1

    return passs


def entropy_check(pass_length, pool_size):
    return round(pass_length * math.log2(pool_size), 2)


def password_generate(left, right, PASSWORD_LENGTH):
    passwd = []
    pick = MyRandom(seed=(right - left))

    passwd.append(pick.pick_char(pool["L"]))
    passwd.append(pick.pick_char(pool["U"]))
    passwd.append(pick.pick_char(pool["D"]))
    passwd.append(pick.pick_char(pool["S"]))

    while len(passwd) < PASSWORD_LENGTH:
        r = pick.num(right, left)

        if r in [1, 3, 7]:
            passwd.append(pick.pick_char(pool["L"]))
        elif r in [0, 2, 5]:
            passwd.append(pick.pick_char(pool["D"]))
        elif r in [4, 9]:
            passwd.append(pick.pick_char(pool["U"]))
        else:
            passwd.append(pick.pick_char(pool["S"]))

    for i in range(len(passwd) - 1, 0, -1):
        j = int(pick.random() * (i + 1))
        passwd[i], passwd[j] = passwd[j], passwd[i]

    return "".join(passwd)


# --- Test Harness ---
test_cases = [
    {"left": 10, "right": 50, "length": 8},
    {"left": 25, "right": 78, "length": 12},
    {"left": 5, "right": 99, "length": 16},
    {"left": 100, "right": 200, "length": 20}
]

print("Password Generator Test Suite\n")

for i, test in enumerate(test_cases, 1):
    pwd = password_generate(test["left"], test["right"], test["length"])
    dist = charcheck(pwd)
    entropy = entropy_check(test["length"], pool_size)

    print(f"Test Case {i}")
    print("Input:", test)
    print("Password:", pwd)
    print("Length OK:", len(pwd) == test["length"])
    print("Distribution:", dist)
    print("Entropy (bits):", entropy)
    print("-" * 40)
