from application import app, db
from application.models import Games

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()# select * from game>> output is a list : [game1,game2] ..game.name won't work as it is a list so >> game[0].name 
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first() #select * from game LIMIT 1>> output is an object : game1 .. game.name will work as output is an object 
    first_game.name = name #update object 
    db.session.commit() #don't need to add after update just commit 
    return first_game.name