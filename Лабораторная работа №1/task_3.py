list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_of_the_team = len(list_players) // 2        # Индекс середины списка
left_team = list_players[:middle_of_the_team]
right_team = list_players[middle_of_the_team:]

print(left_team)
print(right_team)
