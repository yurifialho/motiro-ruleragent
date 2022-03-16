from spade.agent import Agent
from app.behavihours.monitoreprocessbehav import ProcessMonitorBehav
from app.behavihours.registerintegrationagentsbehav import RegisterIntegrationAgentsBehav
from app.behavihours.monitoreagentsbehav import MonitoreAgentsBehav
from app.behavihours.serverinformationbehav import ServerInformationBehav
from app.util.logger import Logger

from spade.behaviour import OneShotBehaviour
class ChiefAgent(Agent):

    processMonitorBehav = None
    registerIntegrationBehav = None
    monitoreAgents = None
    serverInformation = None

    async def setup(self):
        self.processMonitorBehav = ProcessMonitorBehav()
        self.processMonitorBehav.setupTransitions()
        #self.add_behaviour(self.processMonitorBehav)

        self.registerIntegrationBehav = RegisterIntegrationAgentsBehav()
        #self.registerIntegrationBehav.setupTransitions()
        self.add_behaviour(self.registerIntegrationBehav)

        self.monitoreAgents = MonitoreAgentsBehav()
        self.monitoreAgents.setupTransitions()
        #self.add_behaviour(self.monitoreAgents)

        self.serverInformation = ServerInformationBehav()
        self.serverInformation.setupTransitions()
        #self.add_behaviour(self.serverInformation)

        