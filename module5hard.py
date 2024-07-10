import time


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname in user.nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for title in args:
            self.videos.append(title)

    def get_videos(self, search_word):
        list_titles = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                list_titles.append(video.title)
        return list_titles

    def watch_video(self, film_name):
        if not self.current_user:
            return print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for video in self.videos:
                if film_name in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')

    def __str__(self):
        return f'{self.videos}'


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __hash__(self):
        return self.password

    def __int__(self):
        return self.age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
    ur.add(v1, v2)

# Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

# Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
