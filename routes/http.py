from starlette.requests import Request
from starlette.responses import JSONResponse


class ASGIApplication:
    def __init__(self, scope):
        assert scope["type"] == "http"

    async def __call__(self, receive, send):
        request = Request(scope=self.scope, receive=receive)
        response = JSONResponse({
            "method": request.method,
            "path": request.path,
            "query_params": dict(request.query_params),
        })
        await response(receive, send)