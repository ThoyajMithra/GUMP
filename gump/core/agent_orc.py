from gump.engine.laya.laya_engine import layaDecEng
from gump.core.agent_files import make_files

class Agent:
    def __init__(self):
        self.engine=layaDecEng()

    def agent_files(self):
        make_files()

    def agent_loop(self,state,question=None):
        question= {
            "Request_Type" : {
                "type" : "choice",
                "instructions" : "what is the user requesting?",
                "criteria" : {
                    "Explanation" : "asking to explain something",
                    "Bug Fix" : "requesting to fix something",
                    "others" : "unsure of what the request is"
                }
            }
        }

        self.engine.decide(state,question)
