from app2 import db, Countries, Cities
db.drop_all()
db.create_all() # Creates all table classes defined

uK = Countries(name = 'United Kingdom') #Add example to countries table
db.session.add(uK)
db.session.commit()

# Here we reference the country that london belongs to useing 'country', this is what we named the backref variable in db.relationship()
ldn = Cities(name='London', country = uK)
mcr = Cities(name='Manchester', country = Countries.query.filter_by(name='United Kingdom').first())
print(mcr.country.name)
print(uK.cities[0].name) #grab the index 


db.session.add(ldn)
db.session.add(mcr)
db.session.commit()