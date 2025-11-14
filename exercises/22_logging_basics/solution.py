"""Exercise 22: Logging"""
import logging

def setup_basic_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger

def log_training_progress(logger, epoch, loss):
    logger.info(f"Epoch {epoch}, Loss: {loss}")

def log_error(logger, error_msg):
    logger.error(error_msg)

def log_debug(logger, msg):
    logger.debug(msg)
