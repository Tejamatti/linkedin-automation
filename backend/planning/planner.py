from memory.memory_store import load_memory
from cognition.gpt_engine import generate_message

def plan_next_actions(goal):
    memory = load_memory()
    actions = []
    for profile_id, profile in memory.items():
        if not profile.get("messaged"):
            msg = generate_message(profile["summary"], goal)
            actions.append({
                "type": "message",
                "profile_id": profile_id,
                "message": msg
            })
    return actions
