from datetime import datetime


class Reader:
    count = 0

    def __init__(self, first_name, second_name):
        Reader.count += 1
        self.id = Reader.count
        self.first_name = first_name
        self.second_name = second_name
        self.created_date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def __str__(self):
        return f'{self.id}_{self.first_name}'

    def __repr__(self):
        return f'{self.id}_{self.first_name}'
