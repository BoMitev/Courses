class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_cost = room.expenses + room.room_cost
            if room.budget >= (room.expenses + room.room_cost):
                room.budget -= total_cost
                result.append(f"{room.family_name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(result)

    def status(self):
        result = ""
        result += f"Total population: {sum([r.members_count for r in self.rooms])}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                count = 0
                for c in room.children:
                    result += f"--- Child {count} monthly cost: {(c.cost * 30):.2f}$\n"

            if hasattr(room, 'appliances'):
                app_expenses = 0
                for a in room.appliances:
                    app_expenses += a.get_monthly_expense()
                result += f"--- Appliances monthly cost: {room.expenses:.2f}$\n"

        return result