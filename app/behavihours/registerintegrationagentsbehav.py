from curses.ascii import FS
import time
from tkinter.messagebox import RETRY
from spade.behaviour import CyclicBehaviour
from app.util.logger import Logger

class RegisterIntegrationAgentsBehav(CyclicBehaviour):

    __behaviourPrepared = False

    async def run(self):
        if not self.__behaviourPrepared:
            self.preparePresence()
            self.__behaviourPrepared = True
        time.sleep(10)
        Logger.info("RegisterIntegrationAgentsBehav is running")


    async def on_start(self) -> None:
        Logger.info('Setup Register Integration Agent Behaviour')
        return await super().on_start()

    async def on_end(self) -> None:
        Logger.info('Tear Down Register Integration Agent Behaviour')
        return await super().on_end()

    def preparePresence(self):
        self.presence.set_available()
        self.presence.on_subscribe = self.on_subscribe
        self.presence.on_subscribed = self.on_subscribed
        Logger.info("RegisterIntegrationAgentsBehav was prepared")

    def on_subscribe(self, jid : str) -> None:
        Logger.info(f"Subscribe {jid}")
        self.presence.approve(jid)
        self.presence.subscribe(jid)

    def on_subscribed(self, jid : str) -> None:
        Logger.info(f"Contact List: {self.agent.presence.get_contacts()}")