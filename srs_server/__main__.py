from srs_server import create_app
from srs_server.const import RUN_SETTINGS

if __name__ == '__main__':
    app = create_app("develop")
    app.run(**RUN_SETTINGS)
