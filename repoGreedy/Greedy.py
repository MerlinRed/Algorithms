"""Реализация жадного алгоритма

    необходимо найти минимальное количество станций,
    которые бы покрыли все штаты

    пока список штатов не пуст
    бежим по таблице радиостанций
    ищем одинаковые штаты среди всех штатов и штатов которые покрывает радиостанция
    если количество этих штатов больше тех, которые уже покрыли
    добавляем эту станцию во множество станций, которые необходимо найти
    и убираем покрытые штаты из штатов которые нужно покрыть


"""

states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
stations = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}

final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
