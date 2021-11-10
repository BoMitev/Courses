from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self._table_number

    @table_number.setter
    def table_number(self, value):
        if 51 > value or value > 100:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")

        self._table_number = value
