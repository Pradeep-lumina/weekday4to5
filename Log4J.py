import logging

logging.basicConfig(filename="D:\\Fita class\\Selenium Python\\history.log",
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m%d%Y %I:%M:%S %p')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logging.debug("This is debug message")

logging.info("This is info message")