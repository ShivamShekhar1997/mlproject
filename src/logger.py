# Needed to log whatever exception we face

import os
import logging
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # log file name
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # log path along with name of log file
# getcwd gets current working directory
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE) # entire log file path 

logging.basicConfig( # to override the logging library
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s %(levelname)s - %(message)s",
    level=logging.INFO,
    
)

# if __name__=="__main__":
#     logging.info("Logging has started")