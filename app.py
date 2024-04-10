# Import necessary modules
# Flask for creating our web application
# render_template to render HTML templates
# SocketIO for WebSocket communication
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Create a Flask application instance
app = Flask(__name__)
# Configure a secret key for security purposes
app.config['SECRET_KEY'] = 'your_secret_key'
# Create a SocketIO instance linked to our Flask app
socketio = SocketIO(app)

# Define the root route that serves the main page
@app.route('/')
def index():
    # Serve the HTML file located at `templates/index.html`
    return render_template('index.html')

# Define an event handler for the custom event 'send_message'
@socketio.on('send_message')
def handle_send_message(data):
    # Extract the handle and message from the data sent by the client
    handle = data['handle']
    message = data['message']
    # Combine the handle and message to format it for broadcasting
    full_message = f"{handle}: {message}"
    # Print the message server-side for logging purposes
    print('Message: ' + full_message)
    # Send the full message to all connected clients
    send(full_message, broadcast=True)

# Start the Flask application if this script is the main program
if __name__ == '__main__':
    # Enable WebSocket support in our Flask application
    socketio.run(app)
