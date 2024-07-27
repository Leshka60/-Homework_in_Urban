class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = file_name

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(symbol, '')
                    words = text.split()
                    all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                position = words.index(word.lower()) + 1
                result[file_name] = position
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            count = words.count(word.lower())
            if count > 0:
                result[name] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
