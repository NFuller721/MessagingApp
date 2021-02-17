from flask import Flask, render_template, request
from Packages.ConnectDatabase import ConnectDatabase

# Init flask app
App = Flask(__name__)

# Main app route
@App.route('/')
def index():
    return render_template('index.html')

# Api route
@App.route('/Api', methods=["GET", "POST"])
def Api():
    if request.method == "POST":
        # Connect to Database
        database = ConnectDatabase()
        cursor = database.cursor()

        # Check which is being requested
        Create = True if 'Create' in request.form else False
        Read = True if 'Read' in request.form else False
        Update = True if 'Update' in request.form else False
        Delete = True if 'Delete' in request.form else False

        # If create
        if Create:
            # Get message from post
            message = request.form['message']

            # Insert into database
            cursor.execute(f"INSERT INTO Messages (message) VALUES ('{message}')")
            database.commit()

            # Close database
            database.close()

            # return response
            return {'Response': 'Success!'}
        # If read
        if Read:
            # Get id from post
            id = request.form['id']

            # Check if id is 'All'
            if id == 'All':
                # Get All messages
                cursor.execute("SELECT * FROM Messages")
            # If there is specific id
            else:
                # Get specific message
                cursor.execute(f"SELECT * FROM Messages WHERE id='{id}'")

            # Get post
            posts = cursor.fetchall()

            # Close database
            database.close()

            # Return response and data
            return {'Response': 'Success!', 'Data': [{'id': post[0], 'message': post[1]} for post in posts]}
        # If update
        if Update:
            # Get id and message from post
            id = request.form['id']
            message = request.form['message']

            # Insert into database
            cursor.execute(f"UPDATE Messages SET message='{message}' WHERE id='{id}'")
            database.commit()

            # Close database
            database.close()

            # Return response
            return {'Response': 'Success!'}
        # If delete
        if Delete:
            # Get id from post
            id = request.form['id']

            # Insert into database
            cursor.execute(f"DELETE FROM Messages WHERE id='{id}'")
            database.commit()

            # Close database
            database.close()

            # Return response
            return {'Response': 'Success!'}


        # Return error if no option is chosen
        return {'Error': {'Message': 'No crud request'}}
    # Return error if no post request
    return {'Error': {'Message': 'No request'}}

# If not library
if __name__ == '__main__':
    # Run app
    App.run()
