from paste.deploy import loadapp
from wsgiref.simple_server import make_server


#
# A middleware that adds a key to the environment
# 
class Middleware:

    def __init__(self, app, key="test", value=1):
        self._key = key 
        self._value = value 
        self._app = app 

    def __call__(self, environ, status_response):
        environ[self._key] = self._value
        return self._app(environ, status_response)

#
# This is our application, as usual
#
def application(environ, start_response):

    start_response(
        "200 OK", 
        [("Content-type", "text/html")]
    )

    response = "<html><body><p><b>Environment data:</b></p>"
    response += "<table><tr><th>Key</th><th>Value</th></tr>"
    for key, value in environ.items():
        response +=  "<tr><td>%s</td><td>%s</td></tr>" % ( key, value)
    response = response + "</table></body></html>"
    return [bytes(response, 'utf-8')]
    
#
# This is the factory which is invoked by PasteDeploy, passing 
# additional configuration data from the INI file
#
def app_factory(global_config, **local_conf):
    return application


#
# A filter factory. A filter factory returns a filter function 
#
def filter_factory(global_conf, key):
    # A filter function returns a middleware, wrapping the 
    # provided app
    def filter(app):
        return Middleware(app, key)
    return filter

#
# This call evaluates the INI file and builds an application
#
wsgi_app = loadapp("config:paste.ini", relative_to=".")

httpd = make_server("", 8800, wsgi_app)
httpd.serve_forever()