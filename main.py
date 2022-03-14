import time
import asyncio
import sys
import logging
from spade import quit_spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.template import Template

class RulerAgent(Agent):
    class ReceiveMsgCyclicBehaviour(CyclicBehaviour):
        async def run(self):
            logging.info("Receiving msg...")

            msg = await self.receive(timeout=10)
            if msg:
                logging.info("Message received with content: {}".format(msg.body))
        
        async def on_end(self):
            await self.agent.stop()
    
    async def setup(self):
        a = self.ReceiveMsgCyclicBehaviour()
        self.add_behaviour(a)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # prosodyctl register ruleragent prosody-server ruleragent
    ruleragent = RulerAgent("ruleragent@xmpp-server", "ruleragent")
    future = ruleragent.start(auto_register=True)
    ruleragent.web.start(hostname='ruleragent', port='10001')
    future.result()

    logging.info("Wait until user interrupts with ctrl+C")
    while ruleragent.is_alive():
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logging.info("Stopping...")
            ruleragent.stop()
            break
    quit_spade()