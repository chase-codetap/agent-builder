from fastapi import FastAPI

app = FastAPI(
    title="Multi-Provider Agent Platform",
    description="MVP for multi-provider agents with editable prompts, knowledge ingestion, and agent blueprints.",
    version="0.1.0"
)

# Placeholder for including routers
# from app.api.routes_agents import router as agents_router
# app.include_router(agents_router)
