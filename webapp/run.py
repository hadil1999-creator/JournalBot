from app_folder import app
from app_folder import routes
from app_folder.tracing import trace_request  # Import tracing function


if __name__ == '__main__':
    
    app.run(debug=True)
    trace_request()
