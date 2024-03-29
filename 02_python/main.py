import argparse
import logging
from utils.command_handler import CommandHandler
from utils.command_parser import CommandParser

# TODO 1-1: Use argparse to parse the command line arguments (verbose and log_file). 완
# TODO 1-2: Set up logging and initialize the logger object.

#argparse 모듈 활용
parser = argparse.ArgumentParser()
parser.add_argument('--verbose', type=bool, default=False)
parser.add_argument('--log_path', type=str, default='file_explorer.log')    #객체 생성시여기로 넘겨라!

#logger 모듈 활용
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'

logging.basicConfig(filename= parser.parse_args().log_path, 
                    level=logging.INFO, format=format)

command_parser = CommandParser(parser.parse_args().verbose)

handler = CommandHandler(command_parser)

while True:
    command = input(">> ")
    #input command logger
    logger.info(f"Input command: {command}")  
    handler.execute(command)