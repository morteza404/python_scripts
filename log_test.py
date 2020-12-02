import logging
import os

home = os.getenv(key="HOME")

logname = home + "/Desktop/info.log"

# print(logname)

logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logging.info("Running Urban Planning")

a = 5
b = 0
try:
  c = a / b
except Exception as e:
  logging.exception("Exception occurred")