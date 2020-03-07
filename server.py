from flask import Flask, render_template, url_for, redirect, request
import csv
app = Flask(__name__)


@app.route('/')
def my_home():

    return render_template('index.html')


@app.route('/<string:page_name>')
def my_works(page_name):
    return render_template(page_name)


# @app.route('/about.html')
# def my_about():
#     return render_template('about.html')


# @app.route('/contact.html')
# def my_contact():
#     return render_template('contact.html')


# @app.route('/components.html')
# def my_components():
#     return render_template('components.html')


# @app.route('/work.html')
# def my_work():
#     return render_template('work.html')

# >>>>>. SENDING DATA TO THE SERVER>>>>>
# ...........MAKING A DATABSE AS TEXT FILE..................
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if (request.method == 'POST'):
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:

        return 'something went wrong'
