needed_money = float(input())
number_of_love_lyrics = int(input())
number_of_roses = int(input())
number_keyholders = int(input())
number_cartoon = int(input())
number_lucky_surprise = int(input())

love_lyrics_price = number_of_love_lyrics * 0.6
roses_price = number_of_roses * 7.2
keyholders_price = number_keyholders * 3.6
cartoon_price = number_cartoon * 18.2
lucky_surprise_price = number_lucky_surprise * 22
total_price = love_lyrics_price + roses_price + keyholders_price + cartoon_price +lucky_surprise_price
number_of_articles = number_of_love_lyrics + number_of_roses + number_keyholders + number_cartoon + number_lucky_surprise

if number_of_articles >= 25:
    total_price *= 0.65

hosting_price = total_price * 0.1
profit = total_price - hosting_price
absolute = abs(profit - needed_money)

if profit >= needed_money:
    print(f"Yes! {absolute:.2f} lv left.")
else:
    print(f"Not enough money! {absolute:.2f} lv needed.")
