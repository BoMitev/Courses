class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Test", 5000, 100)

    def test_init_worker(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(5000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_energy_attribute_incrementation(self):
        self.assertEqual(100, self.worker.energy)
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_work_not_enough_energy_raises(self):
        worker = Worker("Test", 5000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual(str(ex.exception), f"Not enough energy.")

    def test_work_money_increased_correctly(self):
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.assertEqual(5000, self.worker.money)

    def test_work_energy_decreased(self):
        self.assertEqual(100, self.worker.energy)
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_worker_get_info_method(self):
        result = self.worker.get_info()
        expected = f"Test has saved 0 money."
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
