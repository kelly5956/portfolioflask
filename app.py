from flask import Flask, render_template, request  #NEW IMPORT -- request
from forms import ContactForm           # NEW IMPORT LINE
from flask.ext.mail import Message, Mail
from wtforms import TextField

mail = Mail()
app = Flask(__name__)    #This is creating a new Flask object

app.secret_key = 'WebDesign'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'umsiwebdesign@gmail.com'
app.config["MAIL_PASSWORD"] = '105sstate'
 
mail.init_app(app)    #This is creating a new Flask object



@app.route('/')          						#This is the main URL
def index():
    return render_template("index.html", name = "index", title = "Home")		#The argument should be in templates folder

@app.route('/keeping')   
def keeping():
	return render_template("keeping.html", name = "keeping", title = "Keeping Up With Kelly")

@app.route('/education')   
def education():
	return render_template("education.html", name = "courses", title = "Education")

@app.route('/resume')   
def resume():
	return render_template("resume.html", name = "resume", title = "Resume")

@app.route('/index')          						
def home():
    return render_template("index.html", name = "index", title = "Home")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':

    msg = Message(form.subject.data, sender='kellyjfischer5@gmail.com', recipients=[form.email.data])
    
    msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
    mail.send(msg);
    form.message.data = ""
    form.subject.data = ""
    form.email.data = ""
    form.name.data = ""
    return render_template('contact.html', form=form, message="Thank you for sumitting your information")
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional
