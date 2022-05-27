# https://docs.python.org/ja/3/howto/logging.html

import logging
logger = logging.getLogger(__name__)

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

sub_logger = logging.getLogger('sub_loger')
sub_logger.setLevel(logging.DEBUG)
sub_logger.addHandler(ch)


logger.error('Logger message')
sub_logger.error('sub Logger message')