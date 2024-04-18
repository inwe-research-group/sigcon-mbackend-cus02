from main import app
from utils.db import db
from utils.ma import ma

db.init_app(app) 
#ma.init_app()

with app.app_context():
    db.create_all()
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")