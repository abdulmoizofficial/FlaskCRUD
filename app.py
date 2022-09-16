from flask import Flask,render_template,request,url_for,redirect

app = Flask(__name__)

db = []

@app.route("/")
def begin():
    return render_template("index.html")
    


@app.route('/edit/<name>', methods = ['POST', 'GET'])
def edit(name):
    for i in db:
        if i["name"] == name:
            return render_template("edit.html", user = i)
    return render_template("index.html")
    
@app.route('/edit', methods = ['POST', 'GET'])
def edit_user():
    if request.method == 'POST':
        for i in range(len(db)):
            print(db[i])
            if db[i]["name"] == request.form['name']:
                db[i]['number'] = request.form['number']
        return render_template("index.html", user = i)
    



@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = {}
        user['name'] = request.form['name']
        user['email'] = request.form['email']
        user['number'] = request.form['number']
        db.append(user)
        return redirect(url_for('home'))
    else:
        return render_template("login.html")

@app.route('/get', methods = ['POST', 'GET'] )
def home():
    return render_template("get.html", users=db)



if __name__ == "__main__":
    app.run(debug=True)