#! /usr/bin/env python3
# steam_store_test.py - test the connectivity of steam store
# author: lwd-temp
# date: 2021-12-26
import contextlib
import logging
import random
import time

import requests

# https://stackoverflow.com/questions/16337511/log-all-requests-from-the-python-requests-module/
try:
    from http.client import HTTPConnection  # py3
except ImportError:
    from httplib import HTTPConnection  # py2


def debug_requests_on():
    """Switches on logging of the requests module."""
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def debug_requests_off():
    """Switches off logging of the requests module, might be some side-effects"""
    HTTPConnection.debuglevel = 0

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.WARNING)
    root_logger.handlers = []
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.WARNING)
    requests_log.propagate = False


@contextlib.contextmanager
def debug_requests():
    """Use with 'with'!"""
    debug_requests_on()
    yield
    debug_requests_off()


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="steam_store_test.log",
)

debug_requests_on()


def get_steam(timeout=10):
    """get steam store page"""
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    req = requests.get(
        "https://store.steampowered.com/", timeout=timeout, headers=headers
    )
    return req


def get_steam_stat(timeout=10):
    """return status code"""
    try:
        return get_steam(timeout).status_code
    except:
        return 999  # any exception will be caught and return 999 as status code


def sleeper():
    """sleep to simulate human behavior"""
    time.sleep(random.randint(1, 10) * 0.1 + 1)


if __name__ == "__main__":
    logging.info("Starting steam_store_test.py")
    max_attempts = 100  # max attempts - customisable
    attempts = 0
    failed_attempts = 0
    timeout = 10  # timeout in seconds - customisable
    logging.info("max_attempts: %s" % max_attempts)
    logging.info("timeout: %s" % timeout)
    if timeout <= 1:
        logging.warning("timeout is too small, it may cause false positive")
    for attno in range(0, max_attempts):
        attempts += 1
        logging.info("Attempt #" + str(attempts))
        status = get_steam_stat()
        if status != 200:
            logging.info("Status code: " + str(status))
            failed_attempts += 1
            logging.warning("Total failed attempts " + str(failed_attempts))
        sleeper()
