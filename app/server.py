import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_mail import Mail, Message
from forms import ContactForm
from lib.vars import *
from lib import tools as t

app = Flask(__name__)

app.config.from_pyfile('lib/pro_config.py')
mail = Mail(app)

# Root Mapping
@app.route('/', methods=['GET', 'POST'])
def index():
	loc = t.get_location()
	zipcode = t.get_zipcode(loc)
	homebase = t.nearest_base(zipcode)
	base_data = None

	for base in ADDRESSES:
		if base['zipcode'] == homebase:
			base_data = base

	form = ContactForm()
	jump=alert= None

	if request.method == 'POST':
		if form.validate() == False:
			jump = "#contact"
			for er in form.errors:
				print(er)
		else:
			msg = Message()
			if request.form['subject']:
				msg.subject = request.form['subject']
			else:
				msg.subject = "E-Portfolio Site Form FeedBack"
			msg.add_recipient(TARGET_EMAIL)
			msg.body = request.form['comments']
			mail.send(msg)
			alert = True
			return render_template('index.html', form=form, jump=jump, alert=alert, homebase=homebase)
	return render_template('index.html', form=form, jump=jump, alert=alert, base_data=base_data)

# Start the server
if __name__ == '__main__':

	# Production
	app.run()

	# Development - Cloud 9
	#app.run(host=os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)), debug=True)