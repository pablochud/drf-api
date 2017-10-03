class corsMiddleware(object):
    def process_response(self, req, resp):
        resp["Access-Control-Allow-Origin"] = "*"
        resp["Content-Type"] = "application/json"
        resp["Access-Control-Allow-Methods"] = "POST, GET"
        return resp
