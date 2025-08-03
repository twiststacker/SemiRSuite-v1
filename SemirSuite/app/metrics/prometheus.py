from prometheus_client import Counter, generate_latest
from fastapi import Request, Response

REQUEST_COUNT = Counter("request_count", "Total HTTP requests")

def setup_metrics(app):
    @app.middleware("http")
    async def count_requests(request: Request, call_next):
        REQUEST_COUNT.inc()
        response = await call_next(request)
        return response

    @app.get("/metrics", tags=["Metrics"])
    async def metrics():
        return Response(generate_latest(), media_type="text/plain")