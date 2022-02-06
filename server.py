from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)
app.secret_key = "Thems that dies the lucky ones!"

# our index route will handle rendering our form
@app.route('/')
def index():
    if 'total_gold' and 'activites' not in session:
        session['total_gold'] = 0
        session['activites'] = ""
    return render_template('index.html', messages=session['activites'])

@app.route('/process_money', methods=['POST'])
def process_gold():
    location = request.form['location']
    current_time=datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')
    print(location)
    if location == "farm":
        gold_this_turn = random.randint(10,20)
    elif location == "cave":
        gold_this_turn = random.randint(5,10)
    elif location == "house":
        gold_this_turn = random.randint(2,5)
    else:
        gold_this_turn = random.randint(-50,50)
    session['total_gold'] += gold_this_turn
    print(gold_this_turn)
    if gold_this_turn >= 0:
        new_message = f"<p class='text-success'>You won {gold_this_turn} gold from {location} {current_time}</p>"
    elif gold_this_turn < 0:
        new_message = f"<p class='text-danger'>Bad luck! You lost {gold_this_turn} gold from {location} {current_time}</p>"
    session['activites'] += new_message
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.