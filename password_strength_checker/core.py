special_set = "!@#$%^&*()}{[]<>/?\\|;:=~"

def detect_sequences(password):
    """
    Counts how many sequential runs exist.
    Example: abc, 123, XYZ → each counts as 1 sequence
    """
    seq_count = 0
    run_length = 1

    for i in range(1, len(password)):
        # Check for ascending ASCII sequence
        if ord(password[i]) == ord(password[i - 1]) + 1:
            run_length += 1
            if run_length == 3:
                seq_count += 1
        else:
            run_length = 1

    return seq_count

def detect_repeats(password):
    """
    Returns True if any character appears more than once
    """
    seen = set()
    for ch in password:
        if ch in seen:
            return True
        seen.add(ch)
    return False

def strength_evaluate(password):
    length = len(password)

    has_upper = False
    has_lower = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch in special_set:
            has_special = True

    repeats = detect_repeats(password)
    sequence_count = detect_sequences(password)

    score = 0

    # Length scoring
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    # Character variety scoring
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_special:
        score += 1

    # Penalties
    if repeats:
        score -= 1
    if sequence_count > 0:
        score -= sequence_count

    # Final rating
    if score <= 1:
        rating = "weak"
    elif score <= 3:
        rating = "medium"
    elif score <= 5:
        rating = "strong"
    else:
        rating = "very strong"

    return {
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "specialcharacter": has_special,
        "repeats": repeats,
        "sequence": sequence_count,
        "rating": rating
    }
