from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'klwjnaildrandomkeyyyyjkbhkbkd'#hard password so attackers can't access your app 

class BasicForm(FlaskForm): #Inheritance imported from flask_wtf
    first_name = StringField('First Name')#enter first name
    last_name = StringField('Last Name') #enter last name 
    submit = SubmitField('Add Name') #botton 

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()  #object based of the BaskettForm Object above 

    if request.method == 'POST': #checking if method is POST or GET request which we specify in the home.html
        first_name = form.first_name.data #get the data that we enter in the form(web(end-user interface)) and asve it as a new variable 
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name" #nothing is entered this will be returned 
        else:
            return 'thank_you' # form on web is filled out correctly then this is returned 

    return render_template('home.html', form=form, message=error) # parse error which is ""(nothing) or  error = "Please sup.....  to message which is referenced in the home.html so it can be displaced on the form(web)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')