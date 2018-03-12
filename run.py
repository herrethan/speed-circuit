from livereload import Server, shell
from app.app import app


if __name__ == '__main__':

    if app.config['ENVIRONMENT'] == 'development':
        server = Server(app.wsgi_app)
        server.watch('./app/static/dist/')
        server.watch('./app/templates/')
        server.serve(liveport=35729, port=5000, host='localhost')
    else:
        app.run()
    # from flask.ext.socketio import SocketIO, send, emit
    # socketio = SocketIO(app)
    # socketio.run(app)

    # @socketio.on('client_connected')
    # def handle_client_connect_event(json):
    #     print('received json: {0}'.format(str(json)))


