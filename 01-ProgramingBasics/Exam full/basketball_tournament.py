name_of_tournament = input()
total_matches = 0
won = 0
lost = 0
while name_of_tournament != "End of tournaments":
    matches = int(input())
    for game in range(1, matches+1):
        points = int(input())
        enemy_points = int(input())
        if points > enemy_points:
            print(f"Game {game} of tournament {name_of_tournament}: win with {points - enemy_points} points.")
            won += 1
        else:
            print(f"Game {game} of tournament {name_of_tournament}: lost with {enemy_points - points} points.")
            lost += 1
    total_matches += matches
    name_of_tournament = input()
else:
    print(f"{won / total_matches*100:.2f}% matches win")
    print(f"{lost / total_matches * 100:.2f}% matches lost")