import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_mail import Mail, Message
from forms import ContactForm
from lib.config.config import *
from lib import tools as t

app = Flask(__name__)

app.config.from_pyfile('lib/config/config.py')
mail = Mail(app)

# Root Mapping
@app.route('/', methods=['GET', 'POST'])
def index():
    
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
            return render_template('index.html', form=form, jump=jump, alert=alert, base_data=base_data)
    return render_template('index.html', form=form, jump=jump, alert=alert, base_data=base_data)

# Start the server
if __name__ == '__main__':
    app.run()
