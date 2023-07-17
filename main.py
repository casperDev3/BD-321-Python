import json
import transform_temp as tt


def isPolindrom(word):
    reverse_word = word[::-1]
    if reverse_word == word:
        return True
    else:
        return False


def cesarCode(txt, key=3):
    with open("alfabet.json", 'r') as file:
        alphabet_data = json.load(file)
    code_in_number = []
    for letter in txt:
        for l in alphabet_data:
            if alphabet_data[f"{l}"] == letter.lower():
                code_in_number.append(int(l) + int(key))

    code_word = ''
    for num in code_in_number:
        if num <= 26:
            code_word += alphabet_data[f"{num}"]
        else:
            code_word += alphabet_data[f"{num - 26}"]

    return code_word.capitalize()


if __name__ == "__main__":
    enter_txt = "Python"
    print(enter_txt)
    print(cesarCode(enter_txt))
