import peewee as pw

myDB = pw.MySQLDatabase("mydb", host="mydb.crhauek3cxfw.us-west-2.rds.amazonaws.com", port=3306, user="user", passwd="password")

class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB

class User(MySQLModel):
    username = pw.CharField()
    # etc, etc


# when you're ready to start querying, remember to connect
myDB.connect()
