# DEBUG 1
# INFO 2
# WARNING 3
# ERROR 4
# CRITICAL 5

import logging

logging.basicConfig(level=logging.DEBUG) # For changing priority level

logger = logging.getLogger('SOME LOGGER NAME')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('mylog.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s") # OUTPUT: INFO - 2021-04-07 11:56:35,243: SOME INFO MESSAGE HERE!
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("SOME DEBUG MESSAGE HERE!")
logger.info("SOME INFO MESSAGE HERE!")
