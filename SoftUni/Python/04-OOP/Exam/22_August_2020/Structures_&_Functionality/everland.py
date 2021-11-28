class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.room_cost + room.expenses

        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        info = []
        for room in self.rooms:
            expenses = room.room_cost + room.expenses
            if room.budget >= expenses:
                room.budget -= expenses
                info.append(f"{room.family_name} paid {expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                info.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(info)

    def status(self):
        all_members = sum([r.members_count for r in self.rooms])
        info = [f"Total population: {all_members}"]

        for room in self.rooms:
            info.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.children:
                count = 0
                for child in room.children:
                    count += 1
                    info.append(f"--- Child {count} monthly cost: {(child.cost * 30):.2f}$")
            if hasattr(room, "appliances"):
                total_appliances_cost = sum([a.get_monthly_expense() for a in room.appliances])
                info.append(f"--- Appliances monthly cost: {total_appliances_cost:.2f}$")

        return '\n'.join(info)