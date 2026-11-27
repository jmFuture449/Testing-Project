def clean_text(line: str) -> str:
    """Normalize a transcript line before splitting it into tokens."""
    return line.lower().replace(",", "").replace(".", "")


def count_tokens(tokens: list[str], counts: dict[str, int]) -> None:
    """Add token occurrences to the word-count mapping."""
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1


def process_transcript(lines: list[str]) -> dict[str, int]:
    """Return word‑count mapping for a chat transcript."""
    counts: dict[str, int] = {}
    for line in lines:
        count_tokens(clean_text(line).split(), counts)
    most_common = max(counts.items(), key=lambda kv: kv[1])
    print(f"Most common word → {most_common[0]} ({most_common[1]})")
    return counts

# Sample input and function call
lines = [
  "Hello, how are you?",
  "I am fine. How are you doing?",
  "I am doing well. Thank you!"
]

# Call the function and store the result
word_counts = process_transcript(lines)

# Print the full word count dictionary
print(word_counts)