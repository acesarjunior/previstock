import psycopg2
import frontend.previstock

hostname = ''
username = ''
password = ''
database = ''


def doQuery( conn ) :
    cur = conn.cursor()
    #cur.execute( "SELECT login, password FROM users" )
    cur.execute( "SELECT * FROM users WHERE login = '"+user+"'")
    global logindb
    logindb = ''
    for login, password in cur.fetchall() :
        #print(login,password)
        logindb = login

user = input('Enter your user:')
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery(myConnection)
myConnection.close()
passwd = input('Enter your password:')

if username == user:
    print("Welcome to Previstock")
    symbol = input('Enter the acronym of your stock:')
else:
    print("no")
