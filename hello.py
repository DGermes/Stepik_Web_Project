CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web',
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=4',
        '--timeout=60',
        'hello:wsgi_application'
    )
}

def wsgi_application(environ, start_response):
    # print(environ['QUERY_STRING'])
    # result = '\r\n'.join(environ['QUERY_STRING'].split('&'))
    result = [bytes(i + '\r\n', encoding='utf8')
              for i in environ['QUERY_STRING'].split('&')]
    # result = [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
    #          encoding="utf8")]
    # print(result)
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    # body = 'Hello, world!'
    start_response(status, headers)
    # return iter([result])
    return result


# environ = {}
# environ["QUERY_STRING"] = 'a=1&c=2&b=3'
# ss = wsgi_application(environ, '')
