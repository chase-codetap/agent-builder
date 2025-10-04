from pydantic import BaseModel
from typing import List, Optional, Dict

class Provider(str):
    pass # Enum: "openai", "anthropic", "google"

class AgentRunRequest(BaseModel):
    agent_id: str
    task: str
    provider: str
    model: str
    temperature: float = 0.3
    tools: Optional[List[str]] = None
    top_k_ctx: Optional[int] = 0
    prompt_overrides: Optional[Dict[str, str]] = None

class PromptBuildRequest(BaseModel):
    task: str
    agent_id: str
    audience: Optional[str] = None
    style: Optional[str] = None
    constraints: Optional[str] = None
    tools: Optional[List[str]] = None
    top_k_ctx: Optional[int] = 0
    prompt_overrides: Optional[Dict[str, str]] = None
    ctx: Optional[List[str]] = None

class AgentUpsert(BaseModel):
    agent_id: str
    base_blueprint_id: str
    display_name: Optional[str] = None
    primary_prompt: Optional[str] = None
    defaults: Optional[Dict[str, str]] = None
