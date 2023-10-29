def find_common_participants(group1, group2, separator=','):
    surname_group1 = group1.split(separator)
    surname_group2 = group2.split(separator)

    set_group1 = set(surname_group1)
    set_group2 = set(surname_group2)

    general_participants = set_group1.intersection(set_group2)
    result = sorted(list(general_participants))

    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, separator='|'))
