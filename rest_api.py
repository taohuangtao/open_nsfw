# -*- coding: utf-8 -*-
from config import app
import logging


logger = logging.getLogger(__name__)

if __name__ == '__main__':
    import sys

    # 加载route
    logger.info("加载route")
    from route import nsfw

    logger.info("slkdjf")
    # flask
    from gevent.pywsgi import WSGIServer
    from gevent import monkey

    monkey.patch_all()
    WSGIServer(('0.0.0.0', 5000), app).serve_forever()
    # app.run()
    # flask end
