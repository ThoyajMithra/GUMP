import laya
from laya import Router

import json

from gump.engine.decision_engine import DecisionEngine

class layaDecEng(DecisionEngine):
    def __init__(self):
        self.router=Router(preload=True)
    
    def decide(self, state, question=None):
        if question is None:
            question=laya.triage_questions()
        res=self.router.predict(state,question)
        print(json.dumps(res,indent=4))



