def camelcase(sentence) :
    """Convert sentence to camelCase"""
    title_case = sentence.title() # upper first letter of each word
    upper_camel_cased = title_case.replace(' ', '') # remove spaces
    # lowercase first letter, join with rest of string
    # slices dont produce index out of bounds errors
    # so this still works on empty strings, strings of length 1

    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]


def banner():
    """display program name"""

    message = 'Awesome camelcase program!'
    stars = '*' * len(message)
    print(f'\n{stars}\n{message}\n{stars}')



def main():
    banner()
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)


if __name__ == '__main__':
    main()