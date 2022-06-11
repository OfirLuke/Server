from flask import Flask, redirect, render_template, url_for, request
app = Flask(__name__)
from forms_data import users

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
                           # hobbies={
                           #     'fName': 'Ofir',
                           #     'lName': 'Luke',
                           # },
                           user={'fName': 'Ofir', 'lName': 'Luke'},
                           destinations=['Argentina', 'Brazil', 'Peru', 'Zanzibar', 'Mexico'],
                           flags=['./static/argentinaFlag.png', './static/brzilFlag.png', './static/peruFlag.png', './static/zanzibarFlag.png', './static/mexicoFlag.png']
                           )

@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2_page():
    current_users = []
    if 'search' in request.args:
        search_data = request.args['search']
        if search_data == '':
            current_users = users
        # else:
        #     for user in users:
        #         if search_data == user.name or search_data == user.email:
        #             current_users.append(user)

    return render_template('assignment3_2.html', current_users=current_users)

if __name__ == '__main__':
    app.run(debug=True)