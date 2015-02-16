from flask import Flask

app = Flask (__name__)

@app.route("/hello")
def hello_world():
  return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
 ## return "Hello {}!".format(name.title())
  html = """
  <h1>
    Hello {}!
  </h1>
  <p>
    Here's a picture of a kitten.  Awww ..
  </p>
  <img src="http://placekitten.com/g/200/300">
"""
  return html.format(name.title())

@app.route("/jedi/<fname>/<lname>")
def hello_jedi(fname,lname):
  jname = lname[0:3] + fname[0:2]
  html = """
  <h1>
    Hello {0} {1}!
    Your Jedi Name is:  {2}
  </h1>
"""
  return html.format(fname.title(), lname.title(), jname.title())

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
  
  