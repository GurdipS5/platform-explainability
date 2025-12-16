import json
from datetime import datetime

def explain_decision(decision):
    return f"""Decision Explanation
--------------------
Action: {decision['action']}
Outcome: {decision['outcome']}
Reason: {decision['reason']}
Time: {decision['timestamp']}
"""

if __name__ == "__main__":
    sample = {
        "action": "deploy",
        "outcome": "denied",
        "reason": "Policy violation: image tag 'latest'",
        "timestamp": datetime.utcnow().isoformat()
    }
    print(explain_decision(sample))
