"""
第5章/apache_with_wsgi/server/wsgi_app.py
"""


def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(output)))
    ]
    start_response(status, response_headers)
    return [output]
