#!/usr/bin/env python3

from wsgiref.simple_server import make_server

class MiddleWare:
    def __init__(self, app):
        self.app = app

    def __call__(self, environment, start_response):
        environment["added_by_middleware"] = 1
        environment["author"] = "morteza"
        environment["say"] = "hello"
        return self.app(environment, start_response)

def application(environment, start_response):
    start_response(
        "200 ok",
        [("Content-type", "text/html")]
    )

    response = "<html><body><p><b>environment data:</b></p>"

    response += "<table><tr><th>Key</th><th>Value</th></tr>"

    for key,value in environment.items():
        response += f"<tr><td>{key}</td><td>{value}</td></tr>"

    response += "</table></body></html>"

    return [bytes(response, "utf-8")]

httpd = make_server(host="localhost", port=8088, app=MiddleWare(application))

httpd.serve_forever()