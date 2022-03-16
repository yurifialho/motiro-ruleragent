from spade.agent import Agent 
from spade.behaviour import OneShotBehaviour
import time

class Ag(Agent):
    
    async def setup(self):
        print("Teste")
        self.presence.set_available()
        self.presence.subscribe("motiro-tuixaua@xmpp-server")

a = Ag("motiro-paresar@xmpp-server",'motiro-paresar')

a.start()


while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break

a.stop()