#base datos
#http://docs.peewee-orm.com/en/latest/peewee/installation.html
#pip install peewee
# o bien git clone https://github.com/coleifer/peewee.git
# cd peewee
# python setup.py install
#python runtests.py
from peewee import *
from datetime import datetime

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database

print("Abriendo base datos")
db.connect()
print("Creando tablas")
db.create_tables([Person, Pet])
#Let’s begin by populating the database with some people. We will use the save() and create() methods to add and update people’s records.
from datetime import date
uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
print("Guardando registro")
registros=uncle_bob.save() # bob is now stored in the database
print("nº registros guardados",registros)
# Returns: 1

grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
print("Guardando registro",grandma)
herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
print("Guardando registro",herb)

grandma.name = 'Grandma L.'
print("Modificando registro",grandma)
grandma.save()  # Update grandma's name in the database.
# Returns: 1

bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

herb_mittens.delete_instance() # he had a great life
# Returns: 1

herb_fido.owner = uncle_bob
herb_fido.save()

#retraivin data
grandma = Person.select().where(Person.name == 'Grandma L.').get()
#o bien
grandma = Person.get(Person.name == 'Grandma L.')

#list records
for person in Person.select():
    print(person.name)
# prints:
# Bob
# Grandma L.
# Herb

query = Pet.select().where(Pet.animal_type == 'cat')
print("Animales igual a cat")
for pet in query:
    print(pet.name, pet.owner.name)
# prints:
# Kitty Bob
# Mittens Jr Herb
query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))

for pet in query:
    print(pet.name, pet.owner.name)

print("Nombres igual a bob")
for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print(pet.name)

for pet in Pet.select().where(Pet.owner == uncle_bob):
    print(pet.name)

#sort
print("sort")
for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):
    print(pet.name)
# prints:
# Fido
# Kitty
for person in Person.select().order_by(Person.birthday.desc()):
    print(person.name, person.birthday)
# prints:
# Bob 1960-01-15
# Herb 1950-05-05
# Grandma L. 1935-03-01

d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Person
         .select()
         .where((Person.birthday < d1940) | (Person.birthday > d1960)))

for person in query:
    print(person.name, person.birthday)

# prints:
# Bob 1960-01-15
# Grandma L. 1935-03-01
query = (Person
         .select()
         .where(Person.birthday.between(d1940, d1960)))
for person in query:
    print(person.name, person.birthday)
# prints:
# Herb 1950-05-05
#agregar
for person in Person.select():
    print(person.name, person.pets.count(), 'pets')
# prints:
# Bob 2 pets
# Grandma L. 0 pets
# Herb 1 pets

db.close()

#segundo ejemplo
#In order to create these models we need to instantiate a SqliteDatabase object. Then we define our model classes, specifying the columns as Field instances on the class.
# create a peewee database instance -- our models will use this database to
# persist information
#http://docs.peewee-orm.com/en/latest/peewee/example.html
DATABASE = 'tweepee.db'
database = SqliteDatabase(DATABASE)

# model definitions -- the standard "pattern" is to define a base model class
# that specifies which database to use.  then, any subclasses will automatically
# use the correct storage.
class BaseModel(Model):
    class Meta:
        database = database

# the user model specifies its fields (or columns) declaratively, like django
class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

# this model contains two foreign keys to user -- it essentially allows us to
# model a "many-to-many" relationship between users.  by querying and joining
# on different columns we can expose who a user is "related to" and who is
# "related to" a given user
class Relationship(BaseModel):
    from_user = ForeignKeyField(User, backref='relationships')
    to_user = ForeignKeyField(User, backref='related_to')

    class Meta:
        # `indexes` is a tuple of 2-tuples, where the 2-tuples are
        # a tuple of column names to index and a boolean indicating
        # whether the index is unique or not.
        indexes = (
            # Specify a unique multi-column index on from/to-user.
            (('from_user', 'to_user'), True),
        )

# a dead simple one-to-many relationship: one user has 0..n messages, exposed by
# the foreign key.  because we didn't specify, a users messages will be accessible
# as a special attribute, User.messages
class Message(BaseModel):
    user = ForeignKeyField(User, backref='messages')
    content = TextField()
    pub_date = DateTimeField()

def create_tables():
    with database:
        database.create_tables([User, Relationship, Message])

create_tables()

try:
    with database.atomic():
        # Attempt to create the user. If the username is taken, due to the
        # unique constraint, the database will raise an IntegrityError.
        user = User.create(
            #username=request.form['username'],
            username="Victor",
            #password=md5(request.form['password']).hexdigest(),
            password="clave",
            #email=request.form['email'],
            email="correo@correo",
            join_date=datetime.now())
        print("Registro insertado")

    # mark the user as being 'authenticated' by setting the session vars
    #auth_user(user)
    #return redirect(url_for('homepage'))

except IntegrityError:
    #flash('That username is already taken')
    print("Registro existente")

#list records
for user in User.select():
    print(user.username)

database.close()




