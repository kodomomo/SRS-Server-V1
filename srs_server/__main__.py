from srs_server import create_app
from srs_server.const import RUN_SETTINGS


app = create_app("develop")
app.run(**RUN_SETTINGS)