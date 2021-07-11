rest_days = int(input())

rest_days_playing = rest_days * 127
working_days_playing = (365 - rest_days) * 63
playing_time = rest_days_playing + working_days_playing
difference = abs(30000 - playing_time)
hours = difference // 60
minutes = difference % 60

if playing_time <= 30000:
    print(f"Tom sleeps well\n{hours} hours and {minutes} minutes less for play")
else:
    print(f"Tom will run away\n{hours} hours and {minutes} minutes more for play")