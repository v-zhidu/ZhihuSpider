import sys

sys.path.append('D:\\Code\\raven_spider\\raven\\')
sys.path.append('D:\\Code\\raven_spider\\raven\\http_client\\')
from raven import Raven
from log_config import SpiderLogging
a = Raven('a', logger=SpiderLogging(name='a').logger)
# a = Raven('a')
