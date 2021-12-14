# COOKIE

import flask
import datetime

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = 'bla bla bla'
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(days=10)

@app.route('/')
def index_page():
    return 'This is home page'


@app.route('/cookie')
def set_cookie():
    if not flask.request.cookies.get('name'):
        res = flask.make_response('Set cookie done!')
        res.set_cookie('name', 'Ivan', max_age=60*60*24*365)
        return res
    else:
        return f'Cookie name = {flask.request.cookies.get("name")}'

@app.route('/delete-cookie')
def delete_cookie():
    res = flask.make_response('Cookie deleted')
    res.set_cookie('name', '', max_age=0)
    return res


# SESSION
@app.route('/visits')
def visit():
    if 'visits' in flask.session:
        flask.session['visits'] = flask.session.get('visits') + 1
    else:
        flask.session['visits'] = 1

    return f'Visits: {flask.session.get("visits")}'


@app.route('/delete-visits')
def delete_visit():
    flask.session.pop('visits')
    return f'Visits deleted'


@app.route('/bug-session')
def bug_session():
    ret = str(flask.session.items())

    names = {'name_1': 'Ivan', 'name_2': 'Petr'}
    if 'names' in flask.session:
        flask.session['names']['name_1'] = 'Anna'
        flask.session.modified = True
    else:
        flask.session['names'] = names

    return ret





if __name__ == '__main__':
    app.run()
