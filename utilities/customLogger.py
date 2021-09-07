import logging


class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\logs\\automation.log", level=logging.INFO,
        # format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        handler = logging.FileHandler(filename='.\\logs\\automation.log')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger
