from flask import Flask, render_template, request
from Packages.ConnectDatabase import ConnectDatabase

App = Flask(__name__)

@App.route('/')
def index():
    return render_template('index.html')

@App.route('/Api', methods=["GET", "POST"])
def Api():
    if request.method == "POST":
        database = ConnectDatabase()
        cursor = database.cursor()

        Create = True if 'Create' in request.form else False
        Read = True if 'Read' in request.form else False
        Update = True if 'Update' in request.form else False
        Delete = True if 'Delete' in request.form else False

        if Create:
            message = request.form['message']

            cursor.execute(f"INSERT INTO Messages (message) VALUES ('{message}')")
            database.commit()
            database.close()

            return {'Response': 'Success!'}
        if Read:
            id = request.form['id']

            if id == 'All':
                cursor.execute("SELECT * FROM Messages")
            else:
                cursor.execute(f"SELECT * FROM Messages WHERE id='{id}'")

            posts = cursor.fetchall()

            database.close()

            return {'Response': 'Success!', 'Data': [{'id': post[0], 'message': post[1]} for post in posts]}
        if Update:
            id = request.form['id']
            message = request.form['message']

            cursor.execute(f"UPDATE Messages SET message='{message}' WHERE id='{id}'")

            database.commit()
            database.close()

            return {'Response': 'Success!'}
        if Delete:
            id = request.form['id']

            cursor.execute(f"DELETE FROM Messages WHERE id='{id}'")

            database.commit()
            database.close()

            return {'Response': 'Success!'}


        return {'Error': {'Message': 'No crud request'}}
    return {'Error': {'Message': 'No request'}}

if __name__ == '__main__':
    App.run()
