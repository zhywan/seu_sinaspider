# -*- coding: utf-8 -*-

# Scrapy settings for sina project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os
import sys
COOKIE="UM_distinctid=15c07943354c8-0e8acba75299ea-5b412f19-e1000-15c07943356a0; SINAGLOBAL=6923444749677.232.1494775774189; wvr=6; YF-Ugrow-G0=5b31332af1361e117ff29bb32e4d8439; SSOLoginState=1508082217; SCF=Au-0ncqPEUka5K9GGf6OW24CTp2jGe8nx00amFHVfbUvD-xAYyADh6nkxXsLlZbllXEHOUQbREmzICAAQDpV8cE.; SUB=_2A2505_J5DeRhGeRI6lEQ9irPwj-IHXVXlWSxrDV8PUNbmtBeLWHXkW8DHylSxkQyt-i6gD3dqWfEpdJdjw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5QIV-4QSfrqpOpFqYT3zYh5JpX5KMhUgL.FozceKepSoB01Ke2dJLoIpjLxKnLBo-L1KqLxKqL1K-LB-eLxKBLBo.L12zt; SUHB=0IIkZMdeYi8j3R; ALF=1539618215; YF-V5-G0=16139189c1dbd74e7d073bc6ebfa4935; wb_cusLike_2613164393=N; _s_tentry=login.sina.com.cn; Apache=4184054493923.961.1508082223953; ULV=1508082223983:16:3:3:4184054493923.961.1508082223953:1508081229005; YF-Page-G0=280e58c5ca896750f16dcc47ceb234ed; UOR=www.baidu.com,vdisk.weibo.com,login.sina.com.cn"
URL="http://weibo.com/3261134763/FjRDe7TPo?from=page_1006053261134763_profile&wvr=6&mod=weibotime"
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'sina'))
BOT_NAME = 'sina'

SPIDER_MODULES = ['sina.spiders']
NEWSPIDER_MODULE = 'sina.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sina (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
RANDOM_UA_TYPE = "random"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sina.middlewares.SinaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'sina.middlewares.RandomUserAgentMiddlware': 1,
   'sina.middlewares.SinaSpiderMiddleware': 543,

}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   #'sina.pipelines.SinaPipeline': 300,
   # 'sina.pipelines.SinaPipeline1': 200,
   # 'sina.pipelines.SinaPipeline2': 100,
   # 'sina.pipelines.SinaPipeline3': 10，
  # 'sina.pipelines.SinaPipeline4': 1
}
DOWNLOAD_DELAY = 1.1

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
