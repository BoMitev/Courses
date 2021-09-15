wining_symbols = ["@", "#", "$", "^"]


def is_jackpot(ticket):
    for wining_symbol in wining_symbols:
        if wining_symbol in ticket:
            if ticket.count(wining_symbol) == 20:
                print(f'ticket "{ticket}" - 10{wining_symbol} Jackpot!')
                return True
    return False


def is_wining_ticket(ticket):
    left_half = ticket[:10]
    right_half = ticket[10:]
    for wining_symbol in wining_symbols:
        if wining_symbol*6 in left_half and wining_symbol*6 in right_half:
            left_symbols_count = left_half.count(wining_symbol)
            right_symbol_count = right_half.count(wining_symbol)
            match_result = min(left_symbols_count, right_symbol_count)
            print(f'ticket "{ticket}" - {match_result}{wining_symbol}')
            return True
    return False


tickets = [x.strip() for x in input().split(", ")]

for ticket in tickets:
    if not len(ticket) == 20:
        print(f"invalid ticket")
        continue
    if is_jackpot(ticket):
        continue
    if is_wining_ticket(ticket):
        continue
    print(f'ticket "{ticket}" - no match')

#cA$a$$$$$$Ca$$$$$$a$