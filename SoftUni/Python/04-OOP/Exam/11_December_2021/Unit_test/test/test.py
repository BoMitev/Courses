from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("TestName")

    def test_initializing_all_attributes(self):
        self.assertEqual("TestName", self.team.name)
        self.assertDictEqual({}, self.team.members)

    def test_initializing_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.team.name = "Name12"

        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member(self):
        self.team.members = {}
        x = self.team.add_member(Ivan=10, Gergi=20)
        self.assertDictEqual({"Ivan": 10, "Gergi": 20}, self.team.members)
        self.assertEqual("Successfully added: Ivan, Gergi", x)

        y = self.team.add_member(Ivan=10)
        self.assertDictEqual({"Ivan": 10, "Gergi": 20}, self.team.members)
        self.assertEqual("Successfully added: ", y)

    def test_remove_member(self):
        self.team.members = {"Ivan": 20}
        x = self.team.remove_member("Ivan")
        self.assertDictEqual({}, self.team.members)
        self.assertEqual("Member Ivan removed", x)

    def test_remove_member_not_exist(self):
        self.team.members = {"Ivan": 20}
        x = self.team.remove_member("Georgi")
        self.assertDictEqual({"Ivan": 20}, self.team.members)
        self.assertEqual("Member with name Georgi does not exist", x)

    def test_gt_method(self):
        team1 = Team("FirstTeam")
        team2 = Team("SecondTeam")
        team2.members = {"Ivan": 20}

        x = team1 < team2
        y = team1 > team2
        self.assertEqual(True, x)
        self.assertEqual(False, y)

    def test_len_method(self):
        team2 = Team("SecondTeam")
        team2.members = {"Ivan": 20}

        x = len(team2)
        self.assertEqual(1, x)

    def test_add_method(self):
        team1 = Team("FirstTeam")
        team2 = Team("SecondTeam")
        team1.members = {"Gergi": 10}
        team2.members = {"Ivan": 20}

        x = team1 + team2
        self.assertEqual("FirstTeamSecondTeam", x.name)
        self.assertEqual({"Gergi": 10, "Ivan": 20}, x.members)

    def test_str_method(self):
        self.team.members = {"Test": 10, "sTest": 20}
        self.assertEqual(f"Team name: TestName\n"
                         f"Member: sTest - 20-years old\n"
                         f"Member: Test - 10-years old", str(self.team))


if __name__ == "__main__":
    main()
