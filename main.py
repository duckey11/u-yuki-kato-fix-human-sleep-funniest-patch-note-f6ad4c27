import os

ENTRY = (
    "Fixed: human sleep starts within minutes of lying down. "
    "Removed the 3 a.m. feature that replayed every embarrassing "
    "thing you've ever said."
)

# RULES gate: entry must be 1-160 characters. Fail loudly instead of
# writing an invalid entry the sealed scorer would reject.
assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, must be 1-160"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
