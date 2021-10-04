line = input()
player_position_skill = {}
total_points = {}

while line != 'Season end':
    tokens = line.split()
    if tokens[1] == '->':
        tokens = ''.join(tokens)
        tokens = tokens.split('->')
        player = tokens[0]
        position = tokens[1]
        skill = int(tokens[2])
        if player not in player_position_skill:
            player_position_skill[player] = {}
            player_position_skill[player][position] = skill
            total_points[player] = skill
        else:
            if position not in player_position_skill[player]:
                player_position_skill[player][position] = skill
                total_points[player] += skill
            else:
                if player_position_skill[player][position] < skill:
                    player_position_skill[player][position] = 0
                    player_position_skill[player][position] += skill
                    total_points[player] -= total_points[player]
                    total_points[player] += skill

    elif tokens[1] == 'vs':
        tokens = ''.join(tokens)
        tokens = tokens.split('vs')
        player_1 = tokens[0]
        player_2 = tokens[1]
        player_1_dict = {}
        player_2_dict = {}
        if player_1 in player_position_skill and player_2 in player_position_skill:
            for key, value in player_position_skill.items():
                if key == player_1:
                    for position, points in value.items():
                        player_1_dict[position] = points

                elif key == player_2:
                    for position, points in value.items():
                        player_2_dict[position] = points

            for p, s in player_1_dict.items():
                if p in player_2_dict:
                    if player_1_dict[p] > player_2_dict[p]:
                        del player_position_skill[player_2]
                        del total_points[player_2]
                        break
                    elif player_2_dict[p] > player_1_dict[p]:
                        del player_position_skill[player_1]
                        del total_points[player_1]
                        break

    line = input()

total_points = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))
for player, points in total_points.items():
    print(f'{player}: {points} skill')
    for key, value in player_position_skill.items():
        value = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
        if player == key:
            for position, skill in value.items():
                print(f'- {position} <::> {skill}')