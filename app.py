from flask import Flask, render_template, request

app = Flask(__name__)


def get_registration():
    return {
        'name': request.form.get('Name', '')
    }
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = get_registration()
        return render_template('success.html', **data)
    return render_template('register.html')


@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        data = get_registration()
        return render_template('success.html', **data)
    return render_template('success.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)