import logging
def infoLog (msg):
    """
    Inserts the message to the log as an info msg
    """
    logger = logging.getLogger("ImperialDatabase")
    logger.setLevel(logging.INFO)
    # create a file handler
    handler = logging.FileHandler('ImperialLog.log')
    handler.setLevel(logging.INFO)
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(handler)
    logger.info(msg)

def errorLog (msg):
    """
    Inserts the message to the log as an error msg
    """
    logger = logging.getLogger("ImperialDatabase")
    logger.setLevel(logging.ERROR)

    # create a file handler
    handler = logging.FileHandler('ImperialLog.log')
    handler.setLevel(logging.ERROR)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)

    logger.error(msg)