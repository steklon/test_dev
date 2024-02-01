def list_processing(mentors_lists):

    all_list = []

    for mentors_list in mentors_lists:
        for mentor in mentors_list:
            all_list.append(mentor)

    all_names_list = []

    for mentor in all_list:
        mentor_name = mentor.split()[0]
        all_names_list.append(mentor_name)

    return all_names_list


def mentors_unique_names(mentors_lists):

    all_names_list = list_processing(mentors_lists)

    unique_names = set(all_names_list)

    all_names_sorted = sorted(unique_names)

    result = f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'.strip()

    return result


def top_3_names(mentors_lists):

    all_names_list = list_processing(mentors_lists)

    unique_names = set(all_names_list)

    popular = []

    for name in unique_names:
        popular.append([name, all_names_list.count(name)])

    popular.sort(key=lambda x: x[1], reverse=True)

    top_3 = popular[0:3]

    top_3_str = str()

    for name, top in top_3:
        top_3_str += f'{name}: {int(top)} раз(а), '

    result = top_3_str[:-2]

    return result


def super_names(mentors_lists, courses_list):

    mentors_names = []

    for m in mentors_lists:
        course_names = []
        for name in m:
            course_names.append(name.split()[0])
        mentors_names.append(course_names)

    pairs = []

    result = str()

    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2:
                continue

            intersection_set = set(mentors_names[id1]).intersection(set(mentors_names[id2]))

            if len(intersection_set) > 0:
                pair = {courses_list[id1], courses_list[id2]}
                if pair not in pairs:
                    pairs.append(pair)
                    all_names_sorted = sorted(intersection_set)
                    result += (f"На курсах '{courses_list[id1]}' "
                               f"и '{courses_list[id2]}' преподают: "
                               f"{', '.join(all_names_sorted)}\n")

    return result.strip()


if __name__ == '__main__':

    courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
               "Frontend-разработчик с нуля"]

    mentors = [
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков", "Роман Гордиенко"],
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]

    # print(mentors_unique_names(mentors))
    #
    # print(top_3_names(mentors))

    print(super_names(mentors, courses))
