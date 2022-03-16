from curses.ascii import FS
import time
from tkinter.messagebox import RETRY
from spade.behaviour import FSMBehaviour, State
from app.util.logger import Logger

class ProcessMonitorBehav(FSMBehaviour):

    FIND_UPDATED_PROCESS = 'FIND_UPDATED_PROCESS'
    PROCESS_UPDATE = 'PROCESS_UPDATE'
    HIBERNATE = 'HIBERNATE'

    async def on_start(self) -> None:
        Logger.info('Setup Process Monitor Behaviour')
        return await super().on_start()

    async def on_end(self) -> None:
        Logger.info('Tear Down Process Monitor Behaviour')
        return await super().on_end()
    
    def setupTransitions(self) -> None:
        self.add_state(name=self.FIND_UPDATED_PROCESS, 
                       state=self.FindUpdatedProcessState(), 
                       initial=True)
        self.add_state(name=self.PROCESS_UPDATE,
                       state=self.ProcessUpdateState())
        self.add_state(name=self.HIBERNATE,
                       state=self.HibernateState())
        self.add_transition(source=self.FIND_UPDATED_PROCESS, dest=self.PROCESS_UPDATE)
        self.add_transition(source=self.PROCESS_UPDATE, dest=self.HIBERNATE)
        self.add_transition(source=self.FIND_UPDATED_PROCESS, dest=self.HIBERNATE)
        self.add_transition(source=self.HIBERNATE, dest=self.FIND_UPDATED_PROCESS)

    class FindUpdatedProcessState(State):

        async def run(self) -> None:
            Logger.info('Find Updated Process Monitor Behaviour')
            time.sleep(5)
            self.set_next_state(ProcessMonitorBehav.PROCESS_UPDATE)

    class ProcessUpdateState(State):

        async def run(self) -> None:
            Logger.info('Process Update')
            time.sleep(5)
            self.set_next_state(ProcessMonitorBehav.HIBERNATE)
    
    class HibernateState(State):

        async def run(self) -> None:
            Logger.info('Hibernate')
            time.sleep(5)
            self.set_next_state(ProcessMonitorBehav.FIND_UPDATED_PROCESS)
