import math

# Character pools (global so all functions can see them)
pool = {
    "L": "abcdefghijklmnopqrstuvwxyz",
    "U": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "S": "!@#$%^&*()}{[]<>/?//|;:=~",
    "D": "1234567890"
}

# Total available character space (used for entropy)
pool_size = sum(len(v) for v in pool.values())


class MyRandom:
    def __init__(self, seed=123456):
        # Internal state (seed controls the entire random sequence)
        self.seed = seed
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32

    def next(self):
        # Core LCG formula
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def random(self):
        # Normalize to range [0, 1)
        return self.next() / self.m

    def pick_char(self, text):
        # Safeguard for empty input
        if not text:
            return None
        index = int(self.random() * len(text))
        return text[index]

    def num(self, num1, num2):
        # Generate a small pseudo-random digit from two inputs
        if num1 == 0 or num2 == 0:
            return 0
        val = int((self.random() * ((num1 * num2) % (num2 // num1 + 1))) % 10)
        return val


def password_generate():
    passwd = []

    # Example external values
    left = 25
    right = 78

    pick = MyRandom(seed=(right - left))
    PASSWORD_LENGTH = 16

    # --- Guarantee at least one of each type ---
    passwd.append(pick.pick_char(pool["L"]))
    passwd.append(pick.pick_char(pool["U"]))
    passwd.append(pick.pick_char(pool["D"]))
    passwd.append(pick.pick_char(pool["S"]))

    # --- Fill the remaining characters ---
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

    # --- Shuffle so placement is not predictable ---
    for i in range(len(passwd) - 1, 0, -1):
        j = int(pick.random() * (i + 1))
        passwd[i], passwd[j] = passwd[j], passwd[i]

    return "".join(passwd), PASSWORD_LENGTH


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
    # Entropy = length * log2(pool_size)
    entropy = pass_length * math.log2(pool_size)
    return round(entropy, 2)


# --- Run core logic ---
# password, length = password_generate()

# print("Password:", password)
# print("Character distribution:", charcheck(password))
# print("Estimated entropy (bits):", entropy_check(length, pool_size))
