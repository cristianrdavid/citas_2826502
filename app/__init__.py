from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
## importar el config
from .config import Config


## crear objeto de aplicacion 
app = Flask (__name__)

##configurar el objeto flask con el config
app.config.from_object(Config)

#objeto SQLALchemy 
db = SQLAlchemy(app)

#ibjeto para las migraciones 
migrate = Migrate(app , db)

#importar los modelos 
from .models import Medico

##ejecutar el objeto
if __name__=='__main__':
    app.run()