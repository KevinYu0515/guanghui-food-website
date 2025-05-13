import logging, colorlog

logger = logging.getLogger('colored_logger')
logger.setLevel(logging.DEBUG)

log_format = '%(log_color)s%(asctime)s - %(levelname)s - %(message)s'
formatter = colorlog.ColoredFormatter(log_format)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
