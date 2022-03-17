import time
from spade.behaviour import OneShotBehaviour
from aioxmpp.stanza import Presence
from app.util.logger import Logger

class RegisterIntegrationAgentsBehav(OneShotBehaviour):

    # --- METHODS OVERRIED ---
    async def run(self):
        self.prepare_presence()

    # ---------------------------

    def prepare_presence(self):
        self.presence.set_available()
        self.presence.on_subscribe = self.on_subscribe
        self.presence.on_subscribed = self.on_subscribed
        self.presence.on_available = self.on_available
        Logger.info("RegisterIntegrationAgentsBehav was prepared")

    def on_subscribe(self, jid : str) -> None:
        Logger.info(f"Subscribe {jid}")
        self.presence.approve(jid)
        self.presence.subscribe(jid)

    def on_subscribed(self, jid : str) -> None:
        Logger.info(f"Contact List: {self.agent.presence.get_contacts()}")

    def on_available(self, jid, stanza : Presence) -> None:
        Logger.info("[{}] Agent {} is available.".format(self.agent.name, jid.split("@")[0]))
