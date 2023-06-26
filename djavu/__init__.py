import os
from quart import Quart

def create_app(test_config=None):
    app = Quart(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'djavu.sqlite'),
    )

    from . import db
    db.init_app(app)

    from djavu.controllers import register
    app.register_blueprint(register.bp)

    return app

