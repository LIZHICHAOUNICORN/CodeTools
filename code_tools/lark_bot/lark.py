import requests
import json

from tools.utils.logger import logger
import tools.config.conf as conf
from tools.utils.time import create_hour_fmt


class LarkReport():

    def __init__(self, send_type=None, report_url=conf.BOT_WEBHOOK):
        self.url = report_url
        self.msg = None

    def pack(self, msg):
        self.msg = msg

    def report(self):
        logger.debug("Notice lark bot")
        if self.msg is None:
            logger.error("can't find content")
            return

        headers = {"Content-type": "application/json"}
        response = requests.post(
            url=self.url,
            data=json.dumps(self.msg, ensure_ascii=False).encode("utf-8"),
            headers=headers,
            timeout=10)
        logger.debug("msg: {}, response : {}, status_code: {}".format(
            json.dumps(self.msg, ensure_ascii=False), response.text,
            response.status_code))
