import logging, os

# Create a Logger
logger = logging.getLogger(__name__)
# Create a  Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Create a Handler
log_handler = logging.FileHandler('%s/pi-watch/pi-watch.log' %(os.getcwd()))

# Attach formatter to handler
log_handler.setFormatter(formatter)
# Attach Handler to Logger
logger.addHandler(log_handler)