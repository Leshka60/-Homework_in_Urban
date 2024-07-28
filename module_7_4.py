# задание по теме "Форматирование строк".

command1 = 'Мастера кода'
team1_num = 5
score_1 = 40
team1_time = 18235.3

command2 = 'Волшебники данных'
team2_num = 6
score_2 = 42
team2_time = 18015.2

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# Использование %:

print('В команде %s, участников %s!' % (command1, team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

# Использование format():

print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('{} решили задачи за {} c!'.format(command2, team2_time))

# Использование f-строк:

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!')
print(f'Результат битвы: {challenge_result}!')
