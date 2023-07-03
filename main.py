if __name__ == "__main__":
    name = "John"
    fatherName = "Patrick"
    surname = "doe"

    user_data = {"name": name, "fathersName": fatherName, "surname": surname,
                 "pib": f"{surname.title()} {name[0].upper()}. {fatherName[0].upper()}.", 'age': 26}

    # reverse
    # print(fatherName[::-1])
    # print(arr[::-1])

    # TUPLE
    arr_names = ("John", "Jerry", "Simmon")



    #SET
    arr_surnames = {"Doe", "Lee", "Chan"}
    arr_surnames.add('Jane')
    print(arr_surnames)
    arr_surnames.remove('Lee')
    print(arr_surnames)

    print(user_data['pib'])


    # # Primitive Date
    # a = 1
    # b = a
    # b += 1
    #
    # print(a, b)
    #
    # # Complex Data
    # c = [1]
    # d = c.copy()
    # d[0] += 1
    #
    # print(c, d)

    users = [
        {
            "name": "John",
            "age": 31
        },
        {
            "name": "Jane",
            "age": 27
        },
        {
            "name": "Jack",
            "age": 15
        },
        {
            "name": "John",
            "age": 31
        }
    ]

    


