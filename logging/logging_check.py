import logging, logging.handlers
import sys
from sys import getsizeof
logger = logging.getLogger()
print(getsizeof(logger))
logger.setLevel(logging.DEBUG)#we can set deug_level at logger level also

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
streamhandler = logging.StreamHandler()
streamhandler.setFormatter(formatter)
memoryhandler = logging.handlers.MemoryHandler(1024*10, logging.DEBUG, streamhandler)
logger.addHandler(memoryhandler)

# filehandler = logging.FileHandler("sample.log")
# filehandler.setLevel(logging.DEBUG)
# filehandler.setFormatter(formatter)
# logger.addHandler(filehandler)

for i in range(1,100):
	logger.debug('This is a test log message'+str(i))
print(getsizeof(logger))
print(getsizeof(streamhandler))
print(getsizeof(logging.handlers))
print(getsizeof(logging))

local_vars = list(locals().items())
for var,obj in local_vars:
	print(var,sys.getsizeof(obj))