import re

def basic_strength(password: str) -> int:
    score = 0

    # length
    if len(password) >= 8:
        score += 20
    if len(password) >= 12:
        score += 10

    # lowercase
    if re.search(r"[a-z]", password):
        score += 15

    # uppercase
    if re.search(r"[A-Z]", password):
        score += 15

    # digits
    if re.search(r"\d", password):
        score += 15

    # special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 15

    # common patterns (penalty)
    common_patterns = ["123", "abc", "qwerty", "password", "000", "111"]
    for p in common_patterns:
        if p in password.lower():
            score -= 20

    if score < 0:
        score = 0
    if score > 100:
        score = 100

    return score


def get_rating(score: int) -> str:
    if score < 40:
        return "Weak"
    elif score < 70:
        return "Medium"
    elif score < 90:
        return "Strong"
    else:
        return "Very Strong"


if __name__ == "__main__":
    pwd = input("Enter a password to analyze: ")

    score = basic_strength(pwd)
    rating = get_rating(score)

    print("\nPassword Strength Report:")
    print(f"Score: {score}/100")
    print(f"Strength: {rating}")

    print("\nSuggestions:")
    if len(pwd) < 12:
        print("- Use at least 12 characters.")
    if not re.search(r"[A-Z]", pwd):
        print("- Add uppercase letters.")
    if not re.search(r"[a-z]", pwd):
        print("- Add lowercase letters.")
    if not re.search(r"\d", pwd):
        print("- Add some numbers.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        print("- Add special characters.")
