

def wsgi_application(environ, start_response):
    result = '\r\n'.join(environ['QUERY_STRING'].split('&'))

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    # body = 'Hello, world!'
    start_response(status, headers)
    return iter([result])
