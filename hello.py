

def wsgi_application(environ, start_response):
    # result = '\r\n'.join(environ['QUERY_STRING'].split('&'))
    # result = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    result = [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
                    encoding="utf8")]
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    # body = 'Hello, world!'
    start_response(status, headers)
    # return iter([result])
    return result
