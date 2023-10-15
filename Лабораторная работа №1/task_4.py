users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

visiting_dict = {
    'Общее количество' : 0,
    'Уникальные посещения' : 0
    }
visiting_dict['Общее количество'] = len(users)
visiting_dict['Уникальные посещения'] = len(set(users))

print(visiting_dict)
