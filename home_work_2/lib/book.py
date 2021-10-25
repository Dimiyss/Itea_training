class Book:
    count = 0

    def __init__(self, name, author, published_date, genre):
        Book.count += 1
        self.id = Book.count
        self.name = name
        self.author = author
        self.published_date = published_date
        self.genre = genre
        self.current_place = 0  # 0 - library, else - reader id

    def set_current_place(self, reader_id):
        self.current_place = reader_id

    def __str__(self):
        return f'{self.id}:{self.name}'

    def __repr__(self):
        return f'{self.id}:{self.name}'
