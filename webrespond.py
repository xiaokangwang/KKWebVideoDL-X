from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory
from wheezy.web.handlers.file import file_handler
from wheezy.web.handlers.base import permanent_redirect_handler , redirect_handler
from datetime import timedelta
import webreq
import webReqHander
 

all_urls = [
    url('ping', webReqHander.PingHandler, name='ping'),
    url('webui/{path:any}', file_handler(
            root='gui/',
            age=timedelta(hours=0)), name='default')
]


options = {}
main = WSGIApplication(
    middleware=[
        bootstrap_defaults(url_mapping=all_urls),
        path_routing_middleware_factory
    ],
    options=options
)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    try:
        print('Sever runing')
        make_server('', 8080, main).serve_forever()
    except KeyboardInterrupt:
        pass
    print('\Killed!')