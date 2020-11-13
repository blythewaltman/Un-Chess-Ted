"""File to handle requests between front end and back end"""
from flask import Flask
from flask import Flask, render_template, redirect, url_for, request
from flask import session
from os import environ
import json
import board
import player as p

app = Flask(__name__)
app.secret_key = 'some secret key' #can be changes later


@app.route('/', methods=['GET', 'POST'])
def index():
    """navigate to the single player page or multiplayer page"""
    session['image_dict'] = board.board #get the board dictionary from board.py file
    session['num_clicks'] = 0
    if request.method == 'POST':
        if request.form['submit_button'] == 'Single Player':
                return redirect(url_for('singleplayer_setup')) #if the clicked on singleplayer mode
        elif request.form['submit_button'] == 'MultiPlayer':
                return redirect(url_for('multiplayer_setup')) #if the clicked on multiplayer mode
    return render_template('homepage.html')

@app.route('/multiplayer', methods=['GET', 'POST'])
def multiplayer_setup():
    """get and save the players names for multiplayer mode."""
    error = None
    if request.method == 'POST':
        player_one = request.form['firstname']  
        player_two = request.form['secondname']
        session['player1'] = player_one #Use sessions to store data between calls 
        session['player2'] = player_two
        session['player_turn'] = session['player1']
        
        return redirect(url_for('chess')) #call chess()


    return render_template('multiplayer.html', error=error)

@app.route('/singleplayer', methods=['GET', 'POST'])
def singleplayer_setup():
    """get and save the players name and difficulty"""
    error = None
    if request.method == 'POST':
        player_one = request.form['firstname'] #use request.form[] to get the data from html pages
        difficulty = request.form.get('submit_button')
        session['difficulty'] = difficulty
        
        session['player1'] = player_one #save player names
        session['player2'] = "Computer"
        session['player_turn'] = session['player1']
        
        if request.form.get('play') == 'Play': #once the "play" button is pressed, call chess()
            return redirect(url_for('chess'))


        
    return render_template('singleplayer.html', error=error)

      
       
@app.route('/playchess', methods=['GET', 'POST'])
def chess():
    """handle the page where game play occurs
    Future implementation should pass the space selected to the back end to evaluate possible moves. 
    Future implememntation should also pass in the space the piece was moved to in order to evaluate a checkmate or tie. 
    """


    if request.method == 'POST':
        
        session['num_clicks'] += 1
        if int(session['num_clicks']) == 1: #get the space from first click - the space of the piece to move  
            session['start space'] = request.form['space'] #get the space selected
            
            #save the image url from that space
            if session['start space'] in session['image_dict']:
                session['img url'] =  session['image_dict'][session['start space']]
            else:
                session['image_dict'][session['start space']] = ''
                session['img url'] =  ''      

        elif int(session['num_clicks']) == 2: #get the space from second click - the space to move to
            
            session['end space'] = request.form['space'] #get the space to move the piece to
            
            #set the img url on the end space to the img url from the start space
            session['image_dict'][session['end space']] = session['img url']
            session['image_dict'][session['start space']] = "" #remove the img url from the start space
            session['num_clicks']  = 0
            change_turns()
            
            


    json_converted_dict = json.dumps(session['image_dict'])
    return render_template('chess.html', player = session['player_turn'], image_dict = json_converted_dict)

def change_turns():
    """function to handle switching turns. 
    Note: class objects can't be stored within the 'session' dictionary which is why I didn't make a players class.
    """
    if session['player_turn'] == session['player1']:
        session['player_turn'] = session['player2']
    else:
        session['player_turn'] = session['player1']

if __name__ == '__main__':
    app.run(debug=True)