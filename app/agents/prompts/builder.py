# Prompt Builder logic and endpoint

def build_prompt(request):
    # Load blueprint, merge fragments, apply overrides
    return {"messages": [], "plan": [], "self_check": [], "provenance": []}
