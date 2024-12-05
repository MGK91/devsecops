from flask import Flask, request, render_template_string

app = Flask(__name__)

# Vulnerable to XSS: Directly inserting user input into HTML without sanitization
@app.route('/')
def index():
    user_input = request.args.get('input', 'default')
    return render_template_string(f'<h1>Hello, {user_input}</h1>')

# Example of a form accepting user input
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user_input = request.form.get('input')
        return render_template_string(f'<h1>Your input: {user_input}</h1>')
    return '''
        <form method="post">
            <label for="input">Your input:</label>
            <input type="text" name="input" id="input" required>
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
