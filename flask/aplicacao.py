
from wsgiref.simple_server import make_server

def aplicacao(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html;charset=utf-8')])
    html = b"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        
    </body>
    </html>
    """

    return[html]

make_server('', 5000, aplicacao)