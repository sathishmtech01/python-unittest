import logging, logging.handlers
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)#we can set deug_level at logger level also

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
streamhandler = logging.StreamHandler()
streamhandler.setFormatter(formatter)
memoryhandler = logging.handlers.MemoryHandler(1024*10, logging.DEBUG, streamhandler)
logger.addHandler(memoryhandler)

filehandler = logging.FileHandler("sample.log")
filehandler.setLevel(logging.DEBUG)
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

for i in range(1,1000):
	logger.debug('This is a test log message.'+str(i))