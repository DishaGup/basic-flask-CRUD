from flask import Flask, request

app = Flask(__name__)

entries = {}

@app.route('/')
def welcome():
    return "Welcome to my Flask app!"

@app.route('/greet/<username>')
def greet_user(username):
    return f"Hello, {username}!"

@app.route('/farewell/<username>')
def farewell_user(username):
    return f"Goodbye, {username}!"

@app.route('/create', methods=['GET', 'POST'])
def create_entry():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        entries[key] = value
        return f"Entry '{key}': '{value}' created successfully."
    else:
        return '''
        <form method="POST">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key" required><br>
            <label for="value">Value:</label>
            <input type="text" id="value" name="value" required><br>
            <input type="submit" value="Create">
        </form>
        '''

@app.route('/read')
def read_entries():
    if not entries:
        return "No entries found."
    
    result = ""
    for key, value in entries.items():
        result += f"Key: {key}, Value: {value}<br>"
    
    return result

@app.route('/update', methods=['GET', 'POST'])
def update_entry():
    if request.method == 'POST':
        key = request.form['key']
        if key in entries:
            value = request.form['value']
            entries[key] = value
            return f"Entry '{key}' updated successfully."
        else:
            return f"No entry found for key '{key}'."
    else:
        return '''
        <form method="POST">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key" required><br>
            <label for="value">Value:</label>
            <input type="text" id="value" name="value" required><br>
            <input type="submit" value="Update">
        </form>
        '''

@app.route('/delete', methods=['GET', 'POST'])
def delete_entry():
    if request.method == 'POST':
        key = request.form['key']
        if key in entries:
            del entries[key]
            return f"Entry '{key}' deleted successfully."
        else:
            return f"No entry found for key '{key}'."
    else:
        return '''
        <form method="POST">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key" required><br>
            <input type="submit" value="Delete">
        </form>
        '''

if __name__ == '__main__':
    app.run()
