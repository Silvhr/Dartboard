from flask import Flask
from views import views


app = Flask(__name__)
app.register_blueprint(views,url_prefix = "/")
app.add_url_rule("/city", endpoint="city")
if __name__ == '__main__':
    app.run(debug=True,port=8000)
