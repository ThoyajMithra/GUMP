from gump.engine.laya.laya_engine import layaDecEng

class Agent:
    def __init__(self):
        self.engine=layaDecEng()

    def agent_loop(self,state,question=None):
        self.engine.decide(state)

