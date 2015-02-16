from flask import Flask, render_template
from datetime import datetime

app = Flask (__name__)

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """Convert a datetime to a different format."""
    return value.strftime(format)

@app.route("/hello")
def hello_world():
  return render_template('template.html', my_string="Hello World!", current_time=datetime.now())

@app.route("/hello/<name>")
def hello_person(name):
  return render_template('template.html', my_string="Hello " + name + " !", current_time=datetime.now())

@app.route("/jedi/<fname>/<lname>")
def hello_jedi(fname,lname):
  jname = lname[0:3] + fname[0:2]
  full_string = "Your Jedi Name is: " + jname
  return render_template('template.html', my_string=full_string, current_time=datetime.now())

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)
  
  