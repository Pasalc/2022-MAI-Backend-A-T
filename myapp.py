def app(environ, start_response):
    first_string=b"Your Query String:\n"
    query=bytes(environ['QUERY_STRING'],"utf-8")
    last_string=b"\nEnd of Query String:\n"
    data=first_string+query+last_string
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
