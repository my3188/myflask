import os

from flask import Flask, redirect, url_for


def create_app(test_config=None):
    # print('---------------create_app-----------------')
    # print('---->> test_config=', test_config)
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # print('---->> app.instance_path = ', app.instance_path)
    # print('---->> os.path.join = ',
        #   os.path.join(app.instance_path, 'flaskr.sqlite'))
    print('---->> app.config = ', app.config)
    # print('---->> app.config["ENV"] = ', app.config['ENV'])
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        print('----->>  app.config::', app.config);
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    # @app.route('/')
    # def hello():
    #     return redirect(url_for('auth2.login'))
    #     return 'Hello, World! index page'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app



# set FLASK_APP=flaskr
# set FLASK_ENV=development
# flask run
