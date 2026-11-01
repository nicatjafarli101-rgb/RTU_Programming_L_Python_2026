def count_characters(text: str) -> int:
    return sum(1 for char in text if not char.isspace())


def count_words(text: str) -> int:
    return len(text.split())


def extract_numbers(text: str) -> list[int]:
    numbers = []

    for word in text.split():
        cleaned = word.rstrip(".,;:!?")

        if cleaned.startswith("-"):
            digits = cleaned[1:]
        else:
            digits = cleaned

        if digits.isdigit():
            numbers.append(int(cleaned))

    return numbers


def analyze_text(text: str) -> dict:
    numbers = extract_numbers(text)
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0.0

    return {
        "characters": count_characters(text),
        "words": count_words(text),
        "numbers": numbers,
        "sum": total,
        "average": average,
    }


if __name__ == "__main__":
    text = input("Enter text: ")
    result = analyze_text(text)

    print(f"Characters (no spaces): {result['characters']}")
    print(f"Words: {result['words']}")
    print(f"Numbers: {result['numbers']}")
    print(f"Sum: {result['sum']}")
    print(f"Average: {result['average']:.2f}")
