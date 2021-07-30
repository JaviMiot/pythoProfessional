def is_Palindrome(string: str) -> bool:
    string = string.replace(' ', '')
    if string.lower() == string[::-1].lower():
        return True
    return False


def run():
    print(is_Palindrome('ana'))
    print(is_Palindrome(1000))
    print(is_Palindrome('Ana'))
    print(is_Palindrome('lola'))
    print(is_Palindrome('lola'))


if __name__ == '__main__':
    run()
