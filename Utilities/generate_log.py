import logging

class LogGen:

    @staticmethod
    def loggenerate():
        logger = logging.getLogger("names")
        logger.setLevel(logging.DEBUG)
        filehandle = logging.FileHandler("../log_file/logs.log")
        format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        filehandle.setFormatter(format)
        logger.addHandler(filehandle)
        return logger
