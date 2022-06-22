from flask import Flask, redirect
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)


@app.route('/')
def starting_page():  # put application's code here
    return redirect('/home')

@app.route('/home')
def home_page():  # put application's code here
    return render_template('HomePage.html')

@app.route('/onProgress')
def working_on_it():  # put application's code here
    return render_template('workingOnIt.html')

@app.route('/contact')
def contact_page():  # put application's code here
    return render_template('contact.html')

@app.route('/assignment3_1')
def assignment3_1_page():  # put application's code here
    return render_template('assignment3_1.html',
                           hobbies=('Drawing', 'Traveling', 'Eating', 'Dancing', 'Drawing'))

employees = {'emp1': {'name': 'Rihanna', 'email': 'reirei@gmail.com', 'nickname': 'RiRi' },
             'emp2': {'name': 'Shakira', 'email': 'myhipsdontlie@gmail.com', 'nickname': 'Shaki'},
             'emp3': {'name': 'Eminem', 'email': '8miles@gmail.com', 'nickname': 'Slim Shady'},
             'emp4': {'name': 'Sia', 'email': 'ponytailROX@gmail.com', 'nickname': 'Si-Ya'}}

emp_dict = {
    'RiRi': '1234',
    'Shaki': '4321',
    'Slim Shady': '1111',
    'Si-Ya': '4444'
}

@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2_page():  # put application's code here
    if 'name' in request.args:
        name = request.args['name']
        if name == '':
            return render_template('assignment3_2.html',
                                   employees=employees)
        foundEmp = None
        for emp in employees.values():
            if emp['name'] == name:
                foundEmp = emp
                break
        if foundEmp:
            return render_template('assignment3_2.html',
                                   name=foundEmp['name'],
                                   nickname=foundEmp['nickname'],
                                   email=foundEmp['email'])
        else:
            return render_template('assignment3_2.html',
                                   message='Employee not found :(')
    if request.method == 'POST':
        nickname = request.form['nickname']
        password = request.form['password']
        if nickname in emp_dict:
            pas_in_dict = emp_dict[nickname]
            if pas_in_dict == password:
                session['nickname'] = nickname
                session['logedin'] = True
                return render_template('assignment3_2.html',message2='Success', nickname=nickname)
            else:
                return render_template('assignment3_2.html',
                                       message2='Wrong password!')
        else:
            return render_template('assignment3_2.html',
                                   message2='Wrong nickname!')
    return render_template('assignment3_2.html')

@app.route('/log_out')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('assignment3_2_page'))

@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))
#
if __name__ == "__main__":
    app.run()