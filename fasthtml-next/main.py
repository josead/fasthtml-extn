import logging
from fasthtml.common import FastHTMLWithLiveReload, FastHTML, serve

from utils import create_routes

logger = logging.getLogger("app_logger")
logger.level = logging.NOTSET


def create_app(
    *args,
    **kwargs,
) -> FastHTMLWithLiveReload | FastHTML:
    if kwargs.pop("live", False):
        return FastHTMLWithLiveReload(*args, **kwargs)
    kwargs.pop("reload_attempts", None)
    kwargs.pop("reload_interval", None)
    return FastHTML(*args, **kwargs)


app = create_app(live=False)


create_routes((app, app.route))

serve()
