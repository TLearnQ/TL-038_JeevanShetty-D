page = []

def handle_services(service):
    method, path = service.split(" ", 1)

    if method == "GET" and path.startswith("/items?status="):
        status = path.split("=", 1)[1]
        return [t for t in page if t ["status"] == "status"]
    
    if method == "GET" and path == "/items":
        return page
    
    if method == "GET" and path == "/items/count":
        return len(page)
    
    if method == "POST" and path == "/items":
        page_id = len(page) + 1
        page.append({"id":page_id, "name": f"page{page_id}", "status":"available"})
        return "page service is added successfully"
    return "unknown service"

print(handle_services("POST /items"))
print(handle_services("POST /items"))
print(handle_services("POST /items"))
pages[1]["status"]="checked_out"
print(handle_services("GET /items"))
print(handle_services("GET /items/count"))
