pages = []

def handle_request(request):
    method, path = request.split(" ", 1)

    if method == "GET" and path == "/users":
        return pages
    
    if method == "GET" and path == "/users/count":
        return len(pages)
    
    if method == "POST"