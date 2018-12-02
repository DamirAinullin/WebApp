def application(environ, start_response):

    data = "\n".join(environ.get('QUERY_STRING').split("&"))

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])

    return [data]

