# Write a function called stock_availability which receives:
# •	an inventory list of boxes with different kinds of cupcake flavours
# •	"delivery" or "sell" as second parameter
# •	there might or might not be any other parameters – numbers or strings at the end
#
# In case of "delivery"  to the shop was delivered new boxes with diferent kinds of cupcakes:
# •	You should add the boxes at the end of the inventory list
# •	There will be always at least one box delivered
# In case of "sell" Maria has a client and she is selling different boxes with cupcakes:
# •	If there is a number as another parameter, it means that Maria has sold that many boxes with cupcakes and you should remove them from the beginning of the inventory list
# •	If there is/are string/s as another parameter/s, it means that Maria has sold ALL cupcake boxes of the ordered flavour/s.
# Beware that not everything the buyer has ordered might be in stock, so you should check if the order is valid.
# •	If there are no other parameters, it means that Maria has sold only the first box of cupcakes and you should remove  it of the inventory list


def stock_availability(cupcakes, *command):

    if command[0] == "delivery":
        cupcakes += command[1:]
        return cupcakes
    elif command[0] == "sell":
        if len(command) == 1:
            return cupcakes[1:]
        elif isinstance(command[1], int):
            return cupcakes[command[1]:]
        elif isinstance(command[1], str):
            for item in command[1:]:
                cupcakes = list(filter(lambda x: x != item, cupcakes))
            return cupcakes




# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "chocolate", "banana"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
