def create_app(config_file): 

    app = Flask(__name__)    

    app.config.from_file(config_file, toml.load) 

    init_db() 

    configure_logger('log_msg.txt') 

    with app.app_context(): 

        from app.api import index 

        … … … … … … … 

        from app.api import orders 

    return app