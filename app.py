from flask import Flask, redirect, render_template, url_for, request, session
import mysql.connector

app = Flask(__name__)
from forms_data import users

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)


@app.route('/')
def main_page():
    return redirect('/home')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/gallery')
def gallery_page():
    return render_template('gallery.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/contact-us')
def contact_us_page():
    return redirect(url_for('contact_page'))

@app.route('/assignment3_1')
def assignment3_1_page():
    return render_template('assignment3_1.html',
                           user={'fName': 'Ofir', 'lName': 'Luke'},
                           destinations=['ארגנטינה', 'ברזיל', 'פרו', 'זנזיבר', 'מקסיקו'],
                           flags=['./static/argentinaFlag.png', './static/brzilFlag.png', './static/peruFlag.png', './static/zanzibarFlag.png', './static/mexicoFlag.png']
                           )

@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2_page():
    current_users = {}
    message = ''

    if 'search' in request.args:
        search_data = request.args['search']
        if search_data == '':
            current_users = users
        else:
            for user, data in users.items():
                if search_data == data["name"] or search_data == data["email"]:
                    current_users.update({
                        user: users[user]
                    })

    if request.method == 'POST' and len(request.form) > 0:
        user_name = request.form['userName']
        user_email = request.form['email']

        user_registered = False
        for user, data in users.items():
            if user_email == data["email"]:
                message = "אימייל זה כבר קיים במערכת!"
                user_registered = True
                break

        if not user_registered:
            session['username'] = user_name
            session['logedin'] = True
            message = 'משתמש נרשם בהצלחה!'

            num_of_users = len(users) + 1
            new_user_key = 'user{user_number}'.format(user_number=num_of_users)

            users.update({
                new_user_key: {
                    'name': user_name,
                    'email': user_email
                }
            })

    return render_template('assignment3_2.html', current_users=current_users, message=message)

@app.route('/log_out', methods=['GET', 'POST'])
def logout_func():
    print(1)
    session['logedin'] = False
    session.clear()
    return redirect('/assignment3_2')

###### Pages
## assignment4
from pages.assignment4.assignment4 import assignment_4
app.register_blueprint(assignment_4)

if __name__ == '__main__':
    app.run(debug=True)