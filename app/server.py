import os,json

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_mail import Mail, Message
from forms import ContactForm
from lib.config import *
from lib import tools as t

app = Flask(__name__, static_url_path='')

@app.route('.well-known/pki-validation/')
def send():
    return app.send_from_directory('5D4D96B080D656A6B34A29C64894B85.txt')

app.config.from_pyfile('lib/config.py')

mail = Mail(app)

# Root Mapping
@app.route('/', methods=['GET', 'POST'])
def index():
    # Load Resume Data
    resume_data = None
    try:
        with open(FILE_LOC, 'r') as f:
            r = json.load(f)
            resume_data = r[0]
    except IOError:
        print("Error opening :{}\n".format(FILE_LOC))
        raise

    #Unpack Resume Data
    r_fullname = "{} {}. {}".format(resume_data['vitals']['first name'], resume_data['vitals']['middle name'][0],resume_data['vitals']['last name'])

    r_cellphone = None
    for number in resume_data['vitals']['phone']:
        if number['type'] == "mobile":
            #   0 1 2 3 4 5 6 7 8 9
            #   9 2 5 4 7 8 0 3 3 7
            r_cellphone = "({}) {} - {}".format(str(number['number'])[:3], str(number['number'])[3:6], str(number['number'])[6:])
        else:
            r_cellphone = "000-000-0000"

    r_education = resume_data['education']

    r_work = resume_data['experience']

    r_technical = resume_data['technical']

    r_greeting = resume_data['greeting']



    
    # Dynamic or static address?
    base_data = None
    if DYNAMIC_ADDRESS:
        loc = t.get_location(request)
        zipcode = t.get_zipcode(loc)
        homebase = t.nearest_base(zipcode)

        for base in ADDRESSES:
            if base['zipcode'] == homebase:
                base_data = base
                break
    else:
        base_data = ADDRESSES[0]

    # Variables
    form = ContactForm()
    jump=alert= None

    # Contact form
    if request.method == 'POST':
        if form.validate() == False:
            jump = "#contact"
            for er in form.errors:
                print("Error: Form validation/submission error\n\t{}\n".format(er))
        else:
            msg = Message()
            msg.subject = "E-Portfolio Site Form FeedBack"
            msg.add_recipient(TARGET_EMAIL)
            msg.body = request.form['comments']
            mail.send(msg)
            alert = True
            return render_template('index.html', 
                form=form, jump=jump, alert=alert, 
                base_data=base_data)
    return render_template('index.html', form=form, 
        jump=jump, alert=alert, base_data=base_data,
        r_fullname=r_fullname, r_cellphone=r_cellphone,
        r_education=r_education, r_work=r_work, r_technical=r_technical, r_greeting=r_greeting)

# Start the server
if __name__ == '__main__':
    app.run()
