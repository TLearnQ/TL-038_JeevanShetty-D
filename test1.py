tunnel = []

def handle_services(service):
    method, path = service.split(" ", 1)

    if method == "GET" and path.startswith("/items?status="):
        status = path.split("=", 1)[1]
        return [t for t in tunnel if t ["status"] == "status"]
    
    if method == "GET" and path == "/items":
        return tunnel
    
    if method == "GET" and path == "/items/count":
        return len(tunnel)
    
    if method == "POST" and path == "/items":
        tunnel_id = len(tunnel) + 1
        tunnel.append({"id":tunnel_id, "name": f"tunnel{tunnel_id}", "status":"available"})
        return "tunnel service is added successfully"
    return "unknown service"

print(handle_services("POST /items"))
print(handle_services("POST /items"))
print(handle_services("POST /items"))
tunnel[1]["status"]="checked_out"
print(handle_services("GET /items"))
print(handle_services("GET /items/count"))