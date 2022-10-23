from flask import render_template, Flask
app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def login():
    return render_template('Login.html')


@app.route('/welcome', methods=['GET', 'POST'])
def main_menu():
    return render_template('Main_menu.html')


@app.route('/Challenge', methods=['GET', 'POST'])
def challenge_menu():
    return render_template('Challenge.html')


@app.route('/AI', methods=['GET', 'POST'])
def ai_create():
    return render_template('AI_create.html')


@app.route('/Forum')
def forum():
    return render_template('Forum.html')


if __name__ == '__main__':
    app.run(debug=True)

