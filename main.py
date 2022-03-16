import time
from aioxmpp.errors import MultiOSError
from app.util.extras import LogoUtil
from app.agent.chiefagent import ChiefAgent
from app.config.config import Config
from app.util.logger import Logger

if __name__ == "__main__":
    Logger.setup(__name__)
    LogoUtil.info()
    retry = True
    retry_time = 2
    retry_count = 1
    while(retry):
        try:
            
            Logger.info("Initializing Tuixaua Agent.....")
            jid = Config.getXMPPUser()
            Logger.info(f"Connecting with user: {jid}")
            chiefagent = ChiefAgent(Config.getXMPPUser(), Config.getXMPPPass())
            #chiefagent.jid = jid
            future = chiefagent.start(auto_register=True)
            Logger.info("Tuixaua Agent Started.")
            
            if Config.isWebEnabled():
                Logger.info("Initializing Web Interface from Tuixaua Agent.....")
                host = Config.getHostWebName()
                port = Config.getHostWebPort()
                chiefagent.web.start(hostname=host,port=port, templates_path="app/web/templates")
                Logger.info("Web Interface Stated.")
                Logger.info(f"Access: http://{host}:{port}/spade to monitoring.")
            
            future.result()
            retry = False
            Logger.info("Wait until user interrupts with ctrl+C")
            while chiefagent.is_alive():
                try:
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    Logger.info("Stopping...")
                    chiefagent.stop()
                    break
                finally:
                    quit_spade()

        except MultiOSError as err:
            Logger.error(err)
            if retry_count < 3:
                retry_time *= 2
                Logger.info(f"Retry to connect [{retry_count}]. Waiting {retry_time} seconds!")
                time.sleep(retry_time)
                Logger.info(f"Retry to connect [{retry_count}")
                retry_count += 1
            else:
                retry = False
                try:
                    Logger.info("Stopping all services...")
                    chiefagent.kill()
                except:
                    pass
                Logger.error("Cannot connect at XMPP Server. Check your connection!")


    