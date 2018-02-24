from livereload import Server, shell
from app.app import app
from app import views, models


if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('./app/static/dist/')
    server.watch('./app/templates/')
    server.serve(liveport=35729, port=5000, host='localhost')
