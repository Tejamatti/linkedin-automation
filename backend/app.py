from fastapi import FastAPI
from planning.planner import plan_next_actions
from automation.linkedin_bot import send_message

app = FastAPI()

@app.get("/run")
def run_agent(goal: str = "Connect with AI founders"):
    actions = plan_next_actions(goal)
    for act in actions:
        send_message("https://linkedin.com/in/" + act["profile_id"], act["message"])
    return {"status": "completed", "actions": len(actions)}
