from flask import Flask, redirect, render_template, url_for, request, session

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
    registration_data = {}

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
        session['username'] = user_name
        session['logedin'] = True

        num_of_users = len(users) + 1
        new_user_key = 'user{user_number}'.format(user_number=num_of_users)

        users.update({
            new_user_key: {
                'name': user_name,
                'email': user_email
            }
        })

        print(users)

    return render_template('assignment3_2.html', current_users=current_users, registration_data=registration_data)

@app.route('/log_out', methods=['GET', 'POST'])
def logout_func():
    print(1)
    session['logedin'] = False
    session.clear()
    return redirect('/assignment3_2')

# @app.route('assignment3_2/log_in', methods=['GET', 'POST'])
# def login_func():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if username in user_dict:
#             pas_in_dict = user_dict[username]
#             if pas_in_dict == password:
#                 session['username'] = username
#                 session['logedin'] = True
#                 return render_template('log_in.html',
#                                        message='Success',
#                                        username=username)
#             else:
#                 return render_template('log_in.html',
#                                        message='Wrong password!')
#         else:
#             return render_template('log_in.html',
#                                    message='Please sign in!')
#     return render_template('log_in.html')

if __name__ == '__main__':
    app.run(debug=True)