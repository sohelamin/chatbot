from flask import *
import aiml
import os

flask = Flask(__name__)

@flask.route("/")
def hello():
    return render_template('chat.html')

@flask.route("/ask", methods=['POST'])
def ask():
	message = request.form['messageText'].encode('utf-8').strip()

	kernel = aiml.Kernel()

	if os.path.isfile("bot_brain.brn"):
	    kernel.bootstrap(brainFile = "bot_brain.brn")
	else:
	    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
	    kernel.saveBrain("bot_brain.brn")

	# kernel now ready for use
	while True:
	    if message == "quit":
	        exit()
	    elif message == "save":
	        kernel.saveBrain("bot_brain.brn")
	    else:
	        bot_response = kernel.respond(message)
	        # print bot_response
	        return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
