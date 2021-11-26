import logging


class Utils:
    def assertItemFromList(self,list,value):
        for tickets in list:
            print(tickets.get_attribute('id'))
            assert tickets.get_attribute('id') == value
            if tickets.get_attribute('id') == "shmticket":
                tickets.click()
    def custom_logger(self,logLevel=logging.DEBUG):
        # create logger
        logger = logging.getLogger('my_logger')
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)