from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

# @app.route('/fruits', methods=['POST'])
# def fruits():
#     return render_template('fruit.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form['sName'])
    print(request.form['sId'])
    return render_template('checkout.html', sName = request.form['sName'], sId = request.form['sId'], straw = int(request.form['strawQuant']), rasp = int(request.form['raspQuant']), apple = int(request.form['appleQuant']))

@app.route('/fruits')
def fruits():
    return render_template('fruits.html')


if __name__=="__main__":
    app.run(debug=True)