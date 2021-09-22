# un palindromo es una palabra que se le igual al derecho y al revés

def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    print(is_palindrome("ana"))

if __name__ == '__main__':
    run()