from flask import Blueprint, render_template, request, jsonify
import requests
import mysql.connector

# assignment4 blueprint definition
assignment_4 = Blueprint('assignment_4', __name__, static_folder='', template_folder='templates')

# Routes
@assignment_4.route('/assignment4')
def redirect_homepage():
    return render_template('assignment4.html')

# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='myflaskappdb')
    cursor = connection.cursor(named_tuple=True)

    try:
        cursor.execute(query)
    except Exception as e:
        print(e)

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# ------------------------------------------------- #
# -------------------- INSERT --------------------- #
# ------------------------------------------------- #
@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    user_id = request.form['user-id']
    user_name = request.form['user-name']
    user_email = request.form['user-email']

    ## select all user:
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')

    message_for_user = 'משתמש נרשם בהצלחה!'
    for user in users_list:
        if user.id == int(user_id):
            message_for_user = 'תעודת הזהות כבר קיימת במאגר!'

    query = "INSERT INTO users(id, name, email) VALUES ('%s', '%s', '%s')" % (user_id, user_name, user_email)
    interact_db(query=query, query_type='commit')
    return render_template('/assignment4.html', message_for_insert=message_for_user)
# ------------------------------------------------- #
# ------------------------------------------------- #

# ------------------------------------------------- #
# -------------------- DELETE --------------------- #
# ------------------------------------------------- #
@assignment_4.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['user-id-delete']

    ## select all user:
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')

    message_for_user = 'תעודת הזהות לא קיימת במאגר!'

    for user in users_list:
        if user.id == int(user_id):
            message_for_user = 'משתמש נמחק בהצלחה!'

    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query, query_type='commit')
    return render_template('/assignment4.html', message_for_delete=message_for_user)
# ------------------------------------------------- #
# ------------------------------------------------- #


# ------------------------------------------------- #
# -------------------- UPDATE --------------------- #
# ------------------------------------------------- #
@assignment_4.route('/update_user', methods=['POST'])
def update_user_func():
    message_for_user = ""
    user_id = request.form['user-id-update']
    user_name = request.form['user-name-update']
    user_email = request.form['user-email-update']
    if(user_name != "" and user_email != ""):
        query = "UPDATE users SET name='%s', email='%s' WHERE id='%s'" % (user_name, user_email, user_id)
        message_for_user = "שם משתמש ואימייל עודכנו!"
    elif(user_name != "" and user_email == ""):
        query = "UPDATE users SET name='%s' WHERE id='%s'" % (user_name, user_id)
        message_for_user = "שם משתמש עודכן!"
    elif (user_name == "" and user_email != ""):
        query = "UPDATE users SET email='%s' WHERE id='%s'" % (user_email, user_id)
        message_for_user = "אימייל עודכן!"
    else:
        message_for_user = "לא הוכנסו ערכים לשינוי!"
        return render_template('/assignment4.html', message_for_user=message_for_user)

    interact_db(query, query_type='commit')
    return render_template('/assignment4.html', message_for_user=message_for_user)
# ------------------------------------------------- #
# ------------------------------------------------- #

# ------------------------------------------------- #
# ------------------- SELECT ---------------------- #
# ------------------------------------------------- #
@assignment_4.route('/select-users')
def select_users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    print(users_list)
    return render_template('assignment4.html', users=users_list)
# ------------------------------------------------- #
# ------------------------------------------------- #

# ------------------------------------------------- #
# -------------  --- SELECT-JSON ------------------ #
# ------------------------------------------------- #
@assignment_4.route('/assignment4/users')
def select_users_json():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')

    users_object = {}
    for row in users_list:
        print(row)
        users_object[row.id] = {
            'id': row.id,
            'name': row.name,
            'email': row.email,
        }

    print(users_object)
    return jsonify(users_object)
# ------------------------------------------------- #
# ------------------------------------------------- #

@assignment_4.route('/assignment4/outer_source')
def outer_source():
    return render_template('assignment4_outer_source.html')

@assignment_4.route('/assignment4/outer_source/fetch_from_backend')
def outer_source_fetch_data():
    user_number = request.args['user_number_2']
    res = requests.get(f"https://reqres.in/api/users/{user_number}")
    return render_template('assignment4_outer_source.html', request_data=res.json()['data'])

@assignment_4.route('/assignment4/outer_source/')
def outer_source_redirect():
    return

@assignment_4.route('/assignment4/restapi_users')
def restapi_users_without_id():
    return jsonify({
        "id": 0,
        "name": "Default",
        "email": "Default@gmail.com",
    })

@assignment_4.route('/assignment4/restapi_users/<USER_ID>')
def restapi_users(USER_ID):
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    user_exist = False
    users_object = {}

    if not USER_ID.isnumeric():
        return jsonify({
            "message": "Wrong user number!"
        })

    for row in users_list:
        if(row.id == int(USER_ID)):
            user_exist = True
            users_object[row.id] = {
                'id': row.id,
                'name': row.name,
                'email': row.email,
            }

    if not user_exist:
        return jsonify({
            "message": "This user is not exist!"
        })

    return jsonify(users_object)









