import os
from contextlib import suppress
from typing import Optional




def init_log() -> Optional[int]:
    if (log_group := os.environ.get("LOG_GROUP","-1001629153349")) is not None:
        with suppress(ValueError):
            return int(log_group)
    return None


def init_request_timeout() -> int:
    request_timeout = os.environ.get("REQUEST_TIMEOUT", "30")
    with suppress(ValueError):
        return int(request_timeout)
    return 30





class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5879463342:AAHyGLH_1VcBhjljJmLjaGzUD8upxkOUu5o")
    API_ID = int(os.environ.get("API_ID","4682685"))
    API_HASH = os.environ.get("API_HASH","3eba5d471162181b8a3f7f5c0a23c307")
    EXEC_PATH = os.environ.get("GOOGLE_CHROME_SHIM", None)
    # OPTIONAL
    LOG_GROUP = init_log()
    REQUEST_TIMEOUT = init_request_timeout()
    SUPPORT_GROUP_LINK = os.environ.get("SUPPORT_GROUP", "https://t.me/movie_time_botonly")
