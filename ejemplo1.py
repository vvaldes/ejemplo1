#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://github.com/vvaldes/ejemplo1.git

import copy

#import button as button

for i in range(1, 5):
    print(i)

x = input("Enter value:")
print(x)

tempC = input("Enter temp in c:")
tempf = (int(tempC) * 9) / 5 + 32
print(tempf)

s = "abcdefghi"
print(s)
s[1:5]
s.find("def")
print(s)


# answer=""
# while True:
#    answer=input("enter command ,x para terminal:")
#    if answer=="x":
#	break

# print answer
def count_to_n(n):
    for i in range(1, n + 1):
        print(i)


def count(from_num=1, to_num=10):
    for i in range(from_num, to_num + 1):
        print(i)


a = [34, "Fred", 12, False, 72, 3]
print(a)
print(a[1])
a.append("new")
print(a)
a.insert(2, "new2")
print(a)
a.pop(0)
print(a)
for x in a:
    print(x)

for i in range(len(a)):
    print(i, a[i])

b = ["adfasd", "asdfasdf", "grgfg", "zasdfasdf"]
print(b)
b.sort()
print(b)

a = copy.copy(b)
print("a:", a, "b:", b)
d = b[1:3]
print("d:", d)

from datetime import datetime

d = datetime.now()
print("{:%Y-%m-%d %H:%M:%S}".format(d))

f = open("test.txt", "w")
f.write("fichero con esta cadena")
f.close()

f = open("test.txt", "r")
s = f.read()
print(s)

#abre automaticamente y se libera automaticamente
with open("test.txt") as fLectura:
    for linea in fLectura:
        print(linea)


# lista ficheros
# FUNCIONA CON PYTHON3.7  /usr/bin/python3
from os import listdir
from os.path import isfile, isdir


# devuelve lista de nombres, es necesario saber isfile o isdir
def ls1(path):
    return [obj for obj in listdir(path) if isfile(path + obj)]


# no lo encuentra
from os import scandir, getcwd


# devuelve mas informacion del fichero
def ls2(path):
    return [obj.name for obj in scandir(path) if obj.is_file()]


from pathlib import Path


def ls3(path):
    return [obj.name for obj in Path(path).iterdir() if obj.is_file()]


from glob import glob


# retorna con filtro
def ls4(path, filtro=""):
    spath = path + filtro
    return glob(spath)


directorio = "/home/pi/Desktop/libros/"
fichero = directorio + "Annual2018.pdf"
print("Directorio:", directorio)
a = input("Toca Intro")
try:
    files = ls1(directorio)
    for file in files:
        print(file)
except OSError as e:
    print(e.errno)
    print("Error directorio:",directorio, " Fichero:",fichero)

print("Ficheros en el directorio", directorio)
a = input("Toca Intro")
try:
    files = ls2(directorio)
    for file in files:
        print(file)
except OSError as e:
    print(e.errno)
    print("Error directorio:",directorio)

print("Ficheros en el directorio", directorio, )
a = input("Toca Intro")
try:
    files = ls3(directorio)
    for file in files:
        print(file)
except OSError as e:
    print(e.errno)
    print("Error directorio:",directorio)

print("Ficheros en el directorio", directorio, )
a = input("Toca Intro")
ficheros="000*.pdf"
try:
    files = ls4(directorio, ficheros)
    for file in files:
        print(file)
# exit(0)
except OSError as e:
    print(e.errno)
    print("Error directorio:",directorio, " Ficheros:",ficheros)

import random as r

r.randint(1, 6)
print(r.randint(2, 6))

a = r.choice(["a", "c", "d"])
print(a)

import sys

for (i, value) in enumerate(sys.argv):
    print("arg: %d %s " % (i, value))


#escribir fichero csv
import csv
with open("archivo.csv", 'w') as csvfichero:
    escritor = csv.writer(csvfichero)
    escritor.writerow(['María', 'García González', '37'])
    escritor.writerow(['Mario', 'González García', '36'])

import os
os.system("cat archivo.csv")
a = input("Toca Intro")

os.system("rm test.txt")
os.system("rm archivo.csv")

#base datos
#http://docs.peewee-orm.com/en/latest/peewee/installation.html
#pip install peewee
# o bien git clone https://github.com/coleifer/peewee.git
# cd peewee
# python setup.py install
#python runtests.py
from peewee import *

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



import subprocess

ip = subprocess.check_output(['hostname', '-I'])
print("ip:", ip)

import smtplib

gmail_user = "vvaldess@gmail.com"
gmail_pass = "vvgvvgvvg"
smtp_server = "smtp.gmail.com"
smtp_port = 587


def send_email(recipient, subject, text):
    smtpserver = smtplib.SMTP(smtp_server, smtp_port)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_pass)
    header = "To:" + recipient + "\n" + "From:" + gmail_user
    header = header + "\n" + "subject:" + subject
    msg = header + "\n" + text + "\n\n"
    print("Enviando correo header:", header, "mensaje:", msg)
    # comento para no enviar
    # smtpserver.sendmail(gmail_user,recipient,msg)
    smtpserver.close()


send_email("vvaldess@gmail.com", "sub", "esto es un texto")

# EN PYTHON2
# import thread,time,random
# EN PYTHPN3 thread se renombra a _thread
# import threading
import _thread
import time, random


def annoy(message):
    b = 0
    while True:
        b += 1
        time.sleep(random.randint(1, 3))
        print("b:", b, "mensaje:", message)
        if (b > 4):
            break


# thread.start_new(annoy,("800 !!",))
_thread.start_new(annoy, ("800 !!",))
x = 0
while True:
    print(x)
    x += 1
    time.sleep(1)
    if (x > 6):
        break

# servidor web
# apt-get install python-bottle
# ejecutar como sudo ejemplo.py argumentos
# entrar con navegador con ip local o 127.0.0.1
# ctrl+c para salir
# en python3 : sudo pip3 install bottle
#ejecutar como root
from bottle import route, run, template
from datetime import datetime


@route("/")
def index(name="time"):
    dt = datetime.now()
    time = "{:%Y-%m-%d %H:%M:%S}".format(dt)
    return template("<b>Pi thinks the date/time is: {{t}}</b>", t=time)

try:
    run(host="0.0.0.0", port=80)
except PermissionError:
    print("Error de permiso, ejecutar como administrador")

# entradas en rasberry py
# https://www.prometec.net/raspberry-puertas-analogicas/
# https://www.prometec.net/indice-raspberry-pi/
# sudo apt-get install python-smbus
# raspi-config activar i2c y spi
# apt-get install i2c-tools python-serial
# ser=serial.Serial(DEVICE,BAUD)
# detecta entrada
# sudo i2cdetect -y 1

#import serial

#print("abriendo puerto serie ctrl+c para salir")
# ser=serial.Serial("/dev/ttyAMA0",9600)
# ser.write("cualquier texto")

# while True:
#	print(ser.read())

import time
try:
    import RPi.GPIO as gpio
except RuntimeError:
    print("Error importando modudo RPi.GPIO,probablemente necesita acceso superusuario")



gpio.setmode(gpio.BCM)

gpio.setwarnings(False)
for x in range(16, 26):
    gpio.setup(x, gpio.OUT)

for x in range(16, 26):
    print("Encendiendo led n:", x)
    gpio.output(x, True)
    time.sleep(0.15)
    print("Apagando led n:", x)
    gpio.output(x, False)
    time.sleep(0.15)
# liberar pines
gpio.cleanup()

# Ahora tenemos que informar a nuestra Raspberry que vamos a usar nuestro pin 24 como entrada:
gpio.setmode(gpio.BCM)
gpio.setup(24, gpio.IN)

# Esta es la forma mas habitual de definir un pin de la Raspberry como de Afortunadamente, nuestra Raspberry incluye una orden para activar estas resistencias de Pull up internamente y olvidarnos de hardware adicional, haciendo la definicion del pin de marras de esta manera
# Afortunadamente, nuestra Raspberry incluye una orden para activar estas resistencias de Pull up internamente y olvidarnos de hardware adicional, haciendo la definicion del pin de marras de esta manera
gpio.setmode(gpio.BCM)
gpio.setup(24, gpio.IN, pull_up_down=gpio.PUD_DOWN)

# while True:
for x in range(1, 10):
    status = gpio.input(24)
    if status == False:
        print("boton pulsado x:", x)
        time.sleep(0.2)

# Como hacemos para que ademas el LED indique el estado del contacto Esto ya deberias saber hacerlo tomando instrucciones de las ultimas sesiones y te recomiendo que intentes hacerlo por ti mismo, pero por si acaso aqui esta una solucion:
gpio.setmode(gpio.BCM)
gpio.setup(24, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(23, gpio.OUT)

# while True:
for x in range(1, 10):
    status = gpio.input(24)
    if status == False:
        gpio.output(23, True)  # enciende led
        print("boton pulsado x:", x)
        time.sleep(0.3)
        gpio.output(23, False)  # apaga led

# https://www.prometec.net/raspberry-y-pwm/
# Ahora necesitamos crear un objeto el pin 24 que gobernara la modulacion PWM y vamos a llamarla rojo porque ese es el color del led
# gpio.setup(24,gpio.OUT)
# rojo = gpio.PWM(24, 100)
# rojo.start(100)

# Ya solo falta ir modificando el duty cycle o porcentaje util del pulso PWM Como en Arduino mediante la instruccion rojo.ChangeDutyCycle( x )
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(24, gpio.OUT)
rojo = gpio.PWM(24, 100)
rojo.start(100)

# print("Ctrl+c para salir")
# while True:
for x in range(1, 4):
    for i in range(100, -1, -1):
        rojo.ChangeDutyCycle(100 - i)
        time.sleep(0.02)

    print("Ciclo completo")

##libero pines
gpio.cleanup()
rojo.stop()


# en otro momento se utilizara para manejar un servo que es donde mejor se ve las senales moduladas

# rapberry no tiene entradas analogicas, con lo cual podemos conectar un arduino a la entrada usb, aunque tambien hay entradas ADC.
# PROGRAMA ARDUINO PARA ENVIAR POR EL PUERTO USB ENTRADA ANALOGICA
# void setup()
#   { Serial.begin(115200);
#   }

# void loop()
#   { for (int x = 0; x <100 ; x++)
#       {  Serial.print("Lectura arduino ");
#          Serial.print(x);
#          Serial.print(" : ");
#          Serial.println(analogRead(A0));
#          delay(300);
#       }
#   }

# Al conectar el usb arduino a la raspberry realizamos un ls /dev/tty* y vemos las diferencias respecto a no conectarla, la diferencia es el puerto conectado
# supongo que con dmesg sale tambien nuestro puerto es ttyACM0
# Necesitamos abrir un puerto serie
import serial
from serial import SerialException
import time

portName = "/dev/ttyACMA0"

# if portIsUsable(portName):
try:
    arduino = serial.Serial(portName, baudrate=115200, timeout=3.0)

    print("Leyendo puerto serie Arduino por puerto USB:", portName)
    #	while True:
    for x in range(1, 20):
        val = arduino.readline()
        print(val)
    arduino.close()

except SerialException:
    print("Puerto en uso, no se puede abrir puerto:", portName)



#instalar libreria squid
# git clone https://github.com/simonmonk/squid.git
# sudo python3 setup.py install
from squid import *
import time

##libero pines
gpio.cleanup()

try:
    rgb = Squid(18, 23, 24)
    print("pin rojo")
    rgb.set_color(RED)
    time.sleep(2)
    print("pin azul")
    rgb.set_color(BLUE)
    time.sleep(2)
    print("pin verde")
    rgb.set_color(GREEN)
    time.sleep(2)
    print("pin blanco")
    rgb.set_color(WHITE)
    time.sleep(2)
    print("pin blanco intensidad 300")
    rgb.set_color(WHITE,300)
    time.sleep(2)
except KeyboardInterrupt:
    print("gpio abierto ya")

gpio.cleanup()

#si queremos activar algo con un botin
#sudo pip3 install button
#from button import *

#b=button(7)

#while True:
#    if b.is_pressed():
#        print("presionado boton:",time.time())


#while True: # Run forever
#    if gpio.input(10) == GPIO.HIGH:
#        print("Button was pushed!")

#definir evento si pulsa pin 10
def button_callback(channel):
    print("Button was pushed!")

gpio.setwarnings(False) # Ignore warning for now
gpio.setmode(GPIO.BOARD) # Use physical pin numbering
gpio.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
gpio.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter
gpio.cleanup() # Clean up




