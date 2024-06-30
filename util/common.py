import json
import logging
import os
import sys

from loguru import logger as log


def init_loguru(conf_file_path: str):
    """
    initialize the logger
    :param conf_file_path: the json file path
    """
    with open(conf_file_path, "r", encoding="utf-8") as config_file:
        config = json.load(config_file)
        log.remove()
        for handler in config["handlers"]:
            if handler["sink"] in ['sys.stdout', 'stdout']:
                handler["sink"] = sys.stdout
            if handler["sink"] in ['sys.stderr', 'stderr']:
                handler["sink"] = sys.stderr
            log.add(**handler)

        #
        # for handler_config in config.get("handlers", []):
        #     log.add(**handler_config)

        log.info("Init log successfully.")


def uvicorn_log(conf_file_path: str) -> dict:
    """
    init logger for uvicorn.
    :param conf_file_path:
    :return:
    """
    with open(conf_file_path, "r") as f:
        log_config = json.load(f)
        handlers = log_config["handlers"]
        for _, handler in handlers.items():
            if handler['filename']:
               os.makedirs(os.path.dirname(handler['filename']), exist_ok=True)
        logging.config.dictConfig(log_config)
        return log_config
