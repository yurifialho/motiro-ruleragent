import time
import asyncio
import sys
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.template import Template

class RulerAgent(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .", file = sys.stdout)
            self.counter = 0

        async def run(self):
            print("Counter: {}".format(self.counter), file = sys.stdout)
            self.counter += 1
            await asyncio.sleep(1)

    async def setup(self):
        print("Agent starting . . .", file = sys.stdout)
        self.b = self.MyBehav()
        self.a = self.RecevyInformBehav()

        self.add_behaviour(self.b)
        temp = Template()
        temp.set_metadata("performative", "inform")
        self.add_behaviour(self.a, template=temp)

    class RecevyInformBehav(OneShotBehaviour):
        async def run(self):
            print("Receiving msg...")

            msg = None
            while not msg:
                msg = await self.receive(timeout=10)
                print(msg.body)

            await self.agent.stop()

if __name__ == "__main__":
    # prosodyctl register ruleragent prosody-server ruleragent
    dummy = RulerAgent("ruleragent@prosody-server", "ruleragent")
    future = dummy.start()
    future.result()

    print("Wait until user interrupts with ctrl+C", file = sys.stdout)
    while dummy.is_alive():
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping...", file = sys.stdout)
            dummy.stop()
            break