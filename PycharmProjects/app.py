from flask import Flask, url_for, redirect, request, render_template, jsonify

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/dinner', methods=['GET','POST'])
def dinner_selection():
    if request.method == 'POST':
        data = request.get_json()
        print(data['date_val'])
        return jsonify({'success': "added date"})
    elif request.method == 'GET':
        return render_template('calendar.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
