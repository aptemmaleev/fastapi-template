from fastapi import Request
from starlette.responses import JSONResponse

from app.settings import SETTINGS


class AuthMiddleware:        
    async def __call__(self, request: Request, call_next):
        '''Verifies the token in the request header'''
        methods = str(request.url).replace(str(request.base_url), '')
        # Pass homepage
        if methods == '':
            response = await call_next(request)
            return response
        # Pass docs
        if methods in ('docs', 'openapi.json', 'favicon.ico'):
            response = await call_next(request)
            return response    
        # Authorization check
        try:
            token = request.headers["authorization"]
            if self.token == SETTINGS.API_TOKEN:
                response = await call_next(request)
                return response
            else:
                print('INVALID AUTHORIZATION')
            return JSONResponse(content='Invalid Authorization', status_code=401)
        except KeyError as er:
            return JSONResponse(content='Invalid Authorization', status_code=401)