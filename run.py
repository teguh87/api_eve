from app import app
import logging
from logging.handlers import RotatingFileHandler
import hook

if __name__== '__main__':
    handler = RotatingFileHandler('api.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(debug=True)
