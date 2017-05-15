import sys

# sys.path.append('/Users/duzhiqiang/Code/raven-spider/raven')
# sys.path.append('/Users/duzhiqiang/Code/raven-spider/raven/http_client')
from raven import Raven
from log_config import SpiderLogging
a = Raven('a', logger=SpiderLogging(name='a').logger,
          queue='raven.queues.DefaultQueue')
a.start('http://www.zhihu.com')
