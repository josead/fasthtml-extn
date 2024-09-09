import inspect
import logging
from typing import Callable, Type
from fasthtml.core import to_xml
from fasthtml_extn.libraries.tailwind import ExtnHtml
from fasthtml_extn.utils import AppPageDirectory, get_metacall_app_path

logger = logging.getLogger("fasthtml_extn_metacall")


def render_fasthtml_factory(
    path: str, pages: AppPageDirectory
) -> Type[Callable[..., object]]:
    def app():
        p = path
        if not p.startswith("/"):
            p = f"/{p}"
        res = get_metacall_app_path(p, pages)
        return to_xml(ExtnHtml(res))

    return app
