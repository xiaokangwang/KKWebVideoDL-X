from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory
import .webreq


class PingHandler(BaseHandler):

    def get(self):
        response = HTTPResponse()
        response.write('PING_SUCCESS')
        return response


all_urls = [
    url('ping', PingHandler, name='ping'),
    url('', redirect_handler('/webui/index.htm'), name='default'),
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