import dateutil.utils
from flask import Flask, render_template_string, render_template, request

app = Flask(__name__)

FAVICON_URL='https://favicon-generator.org/favicon-generator/htdocs/favicons/2015-01-17/50e4281252565f8fc85151c075d4e937.ico'

@app.route('/<name>')
def Sample(name):
    if name == 'favicon.ico':
        return FAVICON_URL
    else:
        return 'Hello ' + name + "Test"

def log_data(request,details):
    with open('details.log','a') as log:
        print(request.form,request.remote_addr,request.user_agent,details, file=log,sep='|')

@app.route('/EnteredDetails', methods = ['POST'])
def Simple_data():
    Name = request.form['Name']
    Age = request.form['age']
    log_data(request,Name+'&'+Age)
    return render_template('Details.html',
                           Details = 'Entered Details',
                           name = Name,
                           age = Age )
@app.route('/Details/')
@app.route('/Details/<name>')
def accept_details(name=''):
    return render_template('Base.html',
                           The_title = 'Basic Details',
                           default_value=name)
@app.route('/log_data')
def view_log_data():
    with open('details.log','r') as log:
        return render_template('LogDisplay.html',
                               The_title = 'Log Display',
                               the_content = ''.join(log.readlines()).split('|') )

app.run(debug=True)

