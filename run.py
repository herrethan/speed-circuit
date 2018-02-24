from livereload import Server, shell
from app import app


if __name__ == '__main__':
    # app.run(port=5000, use_reloader=True)

    server = Server(app.wsgi_app)
    server.watch('./app/static/dist/')
    server.watch('./app/templates/')
    server.serve(liveport=35729, port=5000, host='localhost')