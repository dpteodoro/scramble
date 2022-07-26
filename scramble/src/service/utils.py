import logging


def get_logger(name, log_level='INFO'):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(logging.StreamHandler())
    return logger
