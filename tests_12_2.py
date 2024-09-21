from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', speed=10)
        self.andrew = Runner('Андрей', speed=9)
        self.nick = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for test, result in cls.all_results.items():
            current_result = {place: participant.name for place, participant in result.items()}
            print(f'{current_result}')

    def test_1(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results['usain, nick'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_2(self):
        tournament = Tournament(90, self.andrew, self.nick)
        result = tournament.start()
        self.all_results['andrew, nick'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_3(self):
        tournament = Tournament(90, self.usain, self.andrew, self.nick)
        result = tournament.start()
        self.all_results['usain, andrew, nick'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
