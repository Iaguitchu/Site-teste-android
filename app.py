from flask import *
from flask_session import Session
from flask_compress import Compress
from config import *
# from blueprints.auth import auth
# from blueprints.page import page

app = Flask(__name__, static_url_path='', static_folder='static')
app.config.from_object(Config)

# app.register_blueprint(auth)
# app.register_blueprint(page)

Session(app)


    

if __name__ in "__main__":
    app.run(host='0.0.0.0', port = 5000)
  
