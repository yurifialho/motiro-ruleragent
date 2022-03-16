from curses.ascii import FS
import time
from tkinter.messagebox import RETRY
from spade.behaviour import FSMBehaviour, State
from app.util.logger import Logger

class ServerInformationBehav(FSMBehaviour):

    WAIT_FOR_CONNECTION = 'WAIT_FOR_CONNECTION'
    PROCESS_REQUEST = 'PROCESS_REQUEST'

    async def on_start(self) -> None:
        Logger.info('Setup Server Information Behaviour')
        return await super().on_start()

    async def on_end(self) -> None:
        Logger.info('Tear Down Server Information Behaviour')
        return await super().on_end()
    
    def setupTransitions(self) -> None:
        self.add_state(name=self.WAIT_FOR_CONNECTION, 
                       state=self.WaitForConnectionState(), 
                       initial=True)
        self.add_state(name=self.PROCESS_REQUEST,
                       state=self.ProcessRequestState())
        self.add_transition(source=self.WAIT_FOR_CONNECTION, dest=self.PROCESS_REQUEST)
        self.add_transition(source=self.PROCESS_REQUEST, dest=self.WAIT_FOR_CONNECTION)

    class WaitForConnectionState(State):

        async def run(self) -> None:
            Logger.info('Wait For Connection Server Information Behaviour')
            time.sleep(5)
            self.set_next_state(ServerInformationBehav.PROCESS_REQUEST)

    class ProcessRequestState(State):

        async def run(self) -> None:
            Logger.info('Process Request')
            time.sleep(5)
            self.set_next_state(ServerInformationBehav.WAIT_FOR_CONNECTION)

