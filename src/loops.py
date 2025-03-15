
def get_long_words(min_word_length: int = 4) -> list[str]:
    sample_words = ['hello', 'world', 'this', 'is', 'a', 'test']
    return [word.upper() for word in sample_words if len(word) > min_word_length]

def main():
    print(get_long_words())

if __name__ == "__main__":
    # python src/loops.py
    main()