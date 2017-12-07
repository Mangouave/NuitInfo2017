
from app import app
#from server import app
# Start application
if __name__ == "__main__":
    app.logger.info("Starting API")
    app.run(debug=DEBUG, host="0.0.0.0", port=5000)