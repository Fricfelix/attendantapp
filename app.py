from flask import Flask

app = Flask(__name__)

migrate = Migrate()
bootstrap = Bootstrap()



if __name__=="main":
	app.run(debug=True)