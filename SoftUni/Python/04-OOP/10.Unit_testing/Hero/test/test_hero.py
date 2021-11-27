from project.hero import Hero

from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Test", 10, 100, 20)
        self.enemy = Hero("EnemyTest", 5, 100, 10)

    def test_initialized_all_attributes(self):
        self.assertEqual("Test", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(20, self.hero.damage)

    def test_battle_with_yourself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_zero_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_if_enemy_hero_with_zero_health(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        self.hero.health = 50
        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)

    def test_battle_win(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual(55, self.hero.health)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(25, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_lose(self):
        self.hero.damage = 1
        self.hero.health = 1
        result = self.hero.battle(self.enemy)

        self.assertEqual(95, self.enemy.health)
        self.assertEqual(6, self.enemy.level)
        self.assertEqual(15, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_str_representation(self):
        self.assertEqual(f"Hero Test: 10 lvl\n"
                         f"Health: 100\n"
                         f"Damage: 20\n", str(self.hero))

if __name__ == "__main__":
    main()
