if __name__ == "__main__":
    credit_data = {
        'user1': {
            'credit1': 5000,
            'credit2': 2000,
            'credit3': 10000
        },
        'user2': {
            'credit1': 3000,
            'credit2': 1500,
            'credit3': 8000
        },
        'user3': {
            'credit1': 7000,
            'credit2': 0,
            'credit3': 5000
        },
        # Додайте інші користувачі та їх кредити сюди
        # ...
        'user20': {
            'credit1': 10000,
            'credit2': 5000,
            'credit3': 3000
        }
    }
    credit_one_count = 0
    credit_two_count = 0
    credit_three_count = 0
    for item in credit_data:
        for credit in credit_data[item]:
            if credit == "credit1":
                credit_one_count += credit_data[item][credit]
            elif credit == "credit2":
                credit_two_count += credit_data[item][credit]
            elif credit == "credit3":
                credit_three_count += credit_data[item][credit]

    print(" Заборговані по Кредиту1: ", credit_one_count)
    print(" Заборговані по Кредиту2: ", credit_two_count)
    print(" Заборговані по Кредиту3: ", credit_three_count)

    for item in credit_data:
        total_debt = 0
        for credit in credit_data[item]:
            total_debt += credit_data[item][credit]

        print(f"{item} --- {total_debt}")

# students = [
#         {
#             "name": "John",
#             "presense": None
#         },
#         {
#             "name": "Jerry",
#             "presense": None
#         },
#         {
#             "name": "Jane",
#             "presense": None
#         }
#
#     ]
#
#     presense_count = 0
#
#     for student in students:
#         flag = True
#         while flag:
#             presense_choice = input(f"Чи є {student['name']} на занятті (Y/N): ")
#             if presense_choice.lower() == "y":
#                 student['presense'] = True
#                 presense_count += 1
#                 flag = False
#             elif presense_choice.lower() == "n":
#                 student['presense'] = False
#                 flag = False
#
#             if flag:
#                 print("Ви обрали не вірне значення, зробіть ваш вибір щераз \n\n")
#
# print(f"Присутні: {presense_count}. Відсутні: {len(students) - presense_count}")

# count_new_student = int(input("Скільки студентів хочете додати: "))
#
# for i in range(count_new_student):
#     name_student = input("Введіть імя нового студента: ")
#     frame_student = {
#        "name": name_student,
#        "presense": None
#     }
#     students.append(frame_student)
