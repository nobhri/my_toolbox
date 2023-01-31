import os
import shutil
import logging
import datetime

# TODO: raise Exception
# TODO: use pytest
# TODO: logger

class file_move:
    def __init__(self, source_path_root, dist_path_root):
        self.source_path_root = "./source"
        self.dist_path_root = "./dist"

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(ch)

        fh = logging.FileHandler('./sample_log.log')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
    def create_file_name(self):
        today = datetime.date.today().strftime('%Y%m%d')
        self.logger.debug('got date today')
        return today + '_text.txt'
    def file_copy(self):
        try:
            shutil.copy(self.source_path_root + '/file.txt', self.dist_path_root +'/'+ self.create_file_name())
            self.logger.info('file coppied')
        except Exception as e:
            self.logger.error(e.args)

if __name__ == '__main__':
    # logger = file_move.the_logger()
    # logger.error('Logger message')
    the_obj = file_move(source_path_root = "./source", dist_path_root = "./dist")
    # today = the_obj.create_file_name()
    # print(today)
    the_obj.file_copy()