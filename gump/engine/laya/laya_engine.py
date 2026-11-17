import httpx
import json

from gump.engine.decision_engine import DecisionEngine

base_url="http://localhost:8000"

class layaDecEng(DecisionEngine):
    def __init__(self):
        # self.router=Router(preload=True)
        pass
    
    def decide(self, state, question=None):
        res=httpx.post(
        f"{base_url}/v1/systemone",
            json={"state" : state,"questions" : question}
        )

        print(json.dumps(res.json(),indent=4))

