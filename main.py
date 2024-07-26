def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def sorted_chars(chars: dict[str, int]) -> list:
    result = []
    for key in chars:
        if key.isalpha():
            result.append({"name": key, "count": chars[key]})
    result.sort(reverse=True, key=lambda x: x["count"])
    return result


def count_chars(text: str) -> dict: 
    result: dict = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in result:
            result[char_lower] += 1
        else:
            result[char_lower] = 1
    return result


def get_book_stats(path):
    text = get_book_text(path)
    words = count_words(text)
    chars = sorted_chars(count_chars(text))

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()
    for chardict in chars:
        print(f"The {chardict["name"]} character was found {chardict["count"]} times")

    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    get_book_stats(book_path)


if __name__ == "__main__":
    main()

