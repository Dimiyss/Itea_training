from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, logout_user, current_user, login_required, login_user

from email_validator import validate_email

from itea_library.library import Library
from itea_library.library_storage.sqlstorage.sqlstorage import SQLStorage

app = Flask(__name__,
            template_folder='../site/templates',
            static_folder='../site/static')

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'a very very secret string =)'

login_manager = LoginManager(app)
login_manager.login_view = 'api_login'


storage = SQLStorage('postgres', 123, 'postgres')

lib = Library(storage)
if not lib.get_all_books():
    lib.load_books_from_txt_file('books.txt', sep='$!$')


@login_manager.user_loader
def load_user(user_id):
    return lib.get_reader_by_id(user_id)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/books', methods=['GET'])
@login_required
def api_get_all_books():
    return render_template('books.html', books=sorted(lib.get_all_books(), key=lambda book: book.id))


@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def api_add_book():
    if request.method == 'POST':
        title_book = request.form.get('title')
        author_book = request.form.get('author')
        year_book = request.form.get('year')

        if not (title_book and author_book and year_book):
            return render_template('add_book.html', message='Введены некорректные данные')
        if not year_book.isnumeric():
            return render_template('add_book.html', message='Введен некорректный год издания')

        ret_code, ret_msg = lib.add_book(title_book, author_book, int(year_book))
        return render_template('add_book.html', message=ret_msg)

    return render_template('add_book.html')

    # WTForm
    # from add_book_form import AddBookForm
    # addBookForm = AddBookForm()
    #
    # if request.method == 'POST':
    #     if addBookForm.validate_on_submit():
    #         print(addBookForm.title.data)
    #         print(addBookForm.author.data)
    #         print(addBookForm.year.data)
    #     else:
    #         print('ERROR!!!!')
    #
    # return render_template('add_book.html', form=addBookForm)


@app.route('/delete_book', methods=['GET', 'POST'])
@login_required
def api_delete_book():
    if request.method == 'POST':
        id_books = [int(i) for i in request.form.keys() if i.isnumeric()]

        if len(id_books):
            message = lib.remove_books(id_books)
            return render_template('delete_book.html',
                                   books=sorted(lib.get_all_books(), key=lambda book: book.id),
                                   message=message)

    return render_template('delete_book.html', books=sorted(lib.get_all_books(), key=lambda book: book.id))


@app.route('/take_book', methods=['GET', 'POST'])
@login_required
def api_take_book():
    if request.method == 'POST':
        id_books = [int(i) for i in request.form.keys() if i.isnumeric()]

        if len(id_books):
            message = lib.give_books(id_books, current_user.get_id())
            return render_template('take_book.html',
                                   books=sorted(lib.get_available_books(), key=lambda book: book.id),
                                   message=message)

    return render_template('take_book.html', books=sorted(lib.get_available_books(), key=lambda book: book.id))


@app.route('/return_book', methods=['GET', 'POST'])
@login_required
def api_return_book():
    if request.method == 'POST':
        id_books = [int(i) for i in request.form.keys() if i.isnumeric()]

        if len(id_books):
            message = lib.return_books(id_books, current_user.get_id())
            return render_template('return_book.html',
                                   books=sorted(lib.get_all_book_from_reader(current_user.get_id()), key=lambda book: book.id),
                                   message=message)

    return render_template('return_book.html',
                           books=sorted(lib.get_all_book_from_reader(current_user.get_id()), key=lambda book: book.id))


@app.route('/registration', methods=['GET', 'POST'])
def api_registration():
    if current_user.is_authenticated:
        flash('Вы уже авторизированы')
        return redirect(url_for('home_page'))

    if request.method == 'POST':
        email = request.form.get('email')
        psw = request.form.get('psw')
        name = request.form.get('name')
        surname = request.form.get('surname')
        year = request.form.get('year')

        if not (email and psw and name and surname and year):
            flash('Введены некорректные данные', 'error')
            return render_template('registration.html')
        if not year.isnumeric():
            flash('Введен некорректный год рождения', 'error')
            return render_template('registration.html')

        try:
            validate_email(email)
        except:
            flash('Введен некорректный email', 'error')
            return render_template('registration.html', message='Введен некорректный email')

        if lib.get_reader_by_email(email):
            flash('Пользователь с таким email уже зарегистрирован', 'error')
            return render_template('registration.html',
                                   message='Пользователь с таким email уже зарегистрирован')

        if lib.add_reader(name, surname, year, email, psw):
            flash('Now you can login')
            return redirect(url_for('api_login'))
        else:
            flash('Now you can login', 'error')
            return render_template('registration.html', message='Error')

    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def api_login():
    if current_user.is_authenticated:
        flash('Вы уже авторизированы')
        return redirect(url_for('home_page'))

    if request.method == 'POST':
        email = request.form.get('email')
        psw = request.form.get('psw')
        next_url = request.args.get('next')

        if not (email and psw):
            flash('Введены некорректные данные', 'error')
            return render_template('login.html')

        reader = lib.get_reader_by_email(email)
        if reader and reader.check_psw(psw):
            login_user(reader)
            if next_url:
                return redirect(next_url)
            return redirect(url_for('home_page'))
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')


@app.route('/logout', methods=['GET'])
@login_required
def api_logout():
    logout_user()
    return redirect(url_for('home_page'))


if __name__ == '__main__':
    app.run()


# CRUD
# C - Create    = POST
# R - Read      = GET
# U - Update    = PUT
# D - Delete    = DELETE