from gump.engine.laya.laya_engine import layaDecEng
from gump.core.agent_files import make_files

class Agent:
    def __init__(self):
        self.engine=layaDecEng()

    def agent_files(self):
        make_files()

    def agent_loop(self,state,question=None):
        self.engine.decide(state)
