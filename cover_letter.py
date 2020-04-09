from flask import Flask, render_template

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD=True

@app.route('/cover_letter/standard')
def standard_cover():
    return render_template("standard.html")

@app.route('/cover_letter/honest')
def honest_cover():
    return render_template("honest.html")

if __name__ == '__main__':
    app.run(debug=True)
