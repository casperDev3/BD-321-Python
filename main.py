def sumNumbers(numOne, numTwo):
    sum = numOne + numTwo
    return sum


def createIntials(name, last_name, fathers_name):
    initials = False
    try:
        initials = f"{last_name.capitalize()} {name[0].upper()}. {fathers_name[0].upper()}."
    except Exception as err:
        print("Сталась помилка в створенні ініціалів!")
    return initials

def runProgram():
    sumNumbers(1, 2)
    intitials = createIntials("Ihor", "Lialiuk", "Roman")
    if intitials:
        print(intitials)
    temperature = int(input("Введіть температуру:"))
    if temperature > 0:
        print("Teplo")
    else:
        print("Cholodno")


if __name__ == "__main__":
    active = True
    while active:
        try:
            runProgram()
        except Exception as err:
            print(err)
        finally:
            ch = input("Чи бажаєте продовжити користування (Y | N): ")
            if ch.lower() == "n":
                active = False

    # try:
    #     num = int("test")
    #     print(num)
    # except Exception as test:
    #     try:
    #         print(test)
    #         print('Сталась помилка при розрахунку ціни')
    #     except Exception as e:
    #         print(e)
    # finally:
    #     print("Some text")
