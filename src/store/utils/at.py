import os
from typing import List

import africastalking


class ATSMSUtil:
    def __init__(self) -> None:
        username = "sandbox"
        api_key = os.environ.get("AT_KEY", default="")
        africastalking.initialize(username, api_key)
        self.sms = africastalking.SMS

    def __callback__(self, error, response):
        if error is not None:
            raise error
        return response

    def send(self, message: str, numbers: List[str]) -> None:
        self.sms.send(message, numbers, callback=self.__callback__)


at_util = ATSMSUtil()
