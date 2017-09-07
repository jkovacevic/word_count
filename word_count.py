import sys
import re


def main():
    assert len(sys.argv) == 2, "Path to input file required"
    path_text = sys.argv[1]
    try:
        word_dict = create_word_dict(path_text)
        display_words(word_dict)
    except TypeError as e:
        # Handle TypeError in certain way.
        print(e, file=sys.stderr)
    except FileNotFoundError as e:
        # Handle FileNotFoundError in certain way.
        print(e, file=sys.stderr)
    except Exception as e:
        # Catch uncaught errors and handle it (e.g. log it).
        print(e, file=sys.stderr)

    return


def create_word_dict(path_text, path_punct="punctuation.txt", buff_size=4096):
    word_dict = {}
    punct_list = get_punctuation_symbols(path_punct)
    with open(path_text, "r") as file_text:
        while True:
            text = get_text_from_file(file_text, buff_size)
            if not text:
                break
            t = clean_text(text, punct_list)

            for word in t.lower().split(" "):
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

    return word_dict


def get_punctuation_symbols(path_punct):
    """ Gets punctuation symbols from file in list """
    plist = None
    with open(path_punct, "r") as f:
        punct_text = f.read()
        if not punct_text:
            raise TypeError("Invalid punctuation file.")
        plist = punct_text.split("\n")

    return plist


def get_text_from_file(file_text, buff_size):
    """ Reads text from file with buffer size bytes. If last few bytes include only
    fragment of word, the same word will be fully included."""
    text = file_text.read(buff_size)
    last_word = text.split(' ')[-1]

    # Word doesn't end with whitespace
    if last_word == last_word.rstrip():
        additional_bytes = []
        while True:
            byte = file_text.read(1)
            if byte in [" ", "\n", "\t", "\r"] or not byte.strip():
                break
            else:
                additional_bytes.append(byte)
        text = text + "".join(additional_bytes)

    return text


def clean_text(text, punct_list):
    """ Cleans text from newlines, standalone and suffix punctuation symbols
    and removes multiple whitespaces. """
    t = re.sub("\n", " ", text)
    t = re.sub("[" + re.escape(''.join(punct_list)) + "]*(\s|$)", " ", t)
    t = re.sub("\s+", " ", t)
    t = t.strip()

    return t


def display_words(word_dict):
    # Sorting is not needed - just for display purposes
    key_list = word_dict.keys()
    for key in sorted(key_list):
        print(key, word_dict[key])


if __name__ == "__main__":
    main()
    pass
