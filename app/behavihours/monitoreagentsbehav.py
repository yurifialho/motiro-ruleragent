from curses.ascii import FS
import time
from tkinter.messagebox import RETRY
from spade.behaviour import FSMBehaviour, State
from app.util.logger import Logger

class MonitoreAgentsBehav(FSMBehaviour):

    CHECKING_AGENTS = 'CHECKING_AGENTS'
    UPDATING_AGENTS = 'UPDATING_AGENTS'

    async def on_start(self) -> None:
        Logger.info('Monitore Agent Behaviour')
        return await super().on_start()

    async def on_end(self) -> None:
        Logger.info('Monitore Agent Behaviour')
        return await super().on_end()
    
    def setupTransitions(self) -> None:
        self.add_state(name=self.CHECKING_AGENTS, 
                       state=self.CheckingAgentsState(), 
                       initial=True)
        self.add_state(name=self.UPDATING_AGENTS,
                       state=self.UpdatingAgentsState())
        self.add_transition(source=self.CHECKING_AGENTS, dest=self.UPDATING_AGENTS)
        self.add_transition(source=self.UPDATING_AGENTS, dest=self.CHECKING_AGENTS)


    class CheckingAgentsState(State):

        async def run(self) -> None:
            Logger.info('Checking Agents Behaviour')
            time.sleep(5)
            if True:
                self.set_next_state(MonitoreAgentsBehav.UPDATING_AGENTS)

    class UpdatingAgentsState(State):

        async def run(self) -> None:
            Logger.info('Register Agent')
            time.sleep(5)
            self.set_next_state(MonitoreAgentsBehav.CHECKING_AGENTS)
