from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, logout_user, current_user, login_required, login_user
import ad_config as cf

from DALibrary.library import Library
from DALibrary.storage.sqlstorage.storage_method import AlchemyStorage

app = Flask(__name__,
            template_folder=cf.TMP_FOLDER,
            static_folder=cf.STATIC_FOLDER)

app.config.from_object('flask_config.ProductionConfig')

login_manager = LoginManager(app)
login_manager.login_view = 'api_user_login'

storage = AlchemyStorage(db_user=cf.BD_USER, db_password=cf.DB_PASSWORD, db_name=cf.DB_NAME)

my_library = Library(storage)


@login_manager.user_loader
def load_user(user_id):
    return my_library.get_reader_by_id(user_id)


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')


@app.route('/book_add', methods=['GET', 'POST'])
@login_required
def api_add_book():
    if request.method == 'POST':
        book_title = request.form.get('title')
        book_author = request.form.get('author')
        book_year = request.form.get('year')
        book_genre = request.form.get('genre')

        if not book_title and not book_author and not book_year and not book_genre:
            return render_template('add_book.html', message='Error!! Mandatory fields not fill. Please repeat!')

        if not book_year.isnumeric():
            return render_template('add_book.html', message='Error!! Wrong published year value. Please repeat!')

        result = my_library.add_book(book_title, book_author, book_year, book_genre)

        return render_template('add_book.html', message=result)

    return render_template('add_book.html')


@app.route('/books', methods=['GET'])
@login_required
def api_all_books():
    return render_template('books.html', books=my_library.get_book_list())


@app.route('/delete_book', methods=['GET', 'POST'])
@login_required
def api_delete_books():
    if request.method == 'POST':
        book_id_list = [int(i) for i in request.form.keys() if i.isnumeric()]
        result = my_library.delete_books(book_id_list)
        return render_template('delete_books.html', books=my_library.get_book_list(), message=result)
    return render_template('delete_books.html', books=my_library.get_book_list())


@app.route('/take_book', methods=['GET', 'POST'])
@login_required
def api_take_book_by_reader():
    if request.method == 'POST':
        book_id_list = [int(i) for i in request.form.keys() if i.isnumeric()]
        print(current_user.get_reader_id())
        result = my_library.give_books(book_id_list, current_user.get_reader_id())
        return render_template('take_book.html', books=my_library.get_available_book_list(), message=result)

    return render_template('take_book.html', books=my_library.get_available_book_list())


@app.route('/return_book', methods=['GET', 'POST'])
@login_required
def api_return_book_by_reader():
    if request.method == 'POST':
        book_id_list = [int(i) for i in request.form.keys() if i.isnumeric()]
        result = my_library.return_books(book_id_list)
        return render_template('return_book.html',
                               books=my_library.get_reader_books(current_user.get_reader_id()),
                               message=result)

    return render_template('return_book.html', books=my_library.get_reader_books(current_user.get_reader_id()))


@app.route('/registration', methods=['GET', 'POST'])
def api_registration():
    if request.method == 'POST':
        reader_first_name = request.form.get('first_name')
        reader_second_name = request.form.get('second_name')
        reader_age = request.form.get('age')
        reader_email = request.form.get('email')
        reader_psw = request.form.get('password')

        if not (reader_first_name and reader_second_name and reader_age and reader_email and reader_psw):
            return render_template('registration.html', message='Error! Miss required fields! Pls, repeat')

        if not (reader_age.isnumeric()):
            return render_template('registration.html', message='Error! Invalid age! Pls, repeat')

        result = my_library.add_reader(reader_first_name, reader_second_name, reader_age, reader_email, reader_psw)
        return redirect(url_for('api_user_login'))

    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def api_user_login():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))

    if request.method == 'POST':
        email = request.form.get('email')
        psw = request.form.get('password')
        next_url = request.args.get('next')

        if not (email and psw):
            return render_template('login.html', message='Error! Miss required fields! Pls, repeat!')

        user = my_library.get_user_by_email(email)
        if user and user.check_psw(psw):
            login_user(user)
            if next_url:
                return redirect(next_url)
            return redirect(url_for('home_page'))
        else:
            return render_template('login.html', message='Error! Invalid email or password! Pls, repeat!')
    return render_template('login.html')


@app.route('/logout', methods=['GET'])
@login_required
def api_user_logout():
    logout_user()
    return redirect(url_for('home_page'))


if __name__ == '__main__':
    app.run()
