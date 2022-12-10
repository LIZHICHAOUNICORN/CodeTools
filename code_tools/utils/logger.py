import logging
# Define logger format
LOG_FORMAT = "%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s %(message)s"
LOG_LEVEL = logging.INFO

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger('cronjob')


def reset_debug_level():
    logger.setLevel(logging.DEBUG)