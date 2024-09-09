import inspect
from fasthtml.core import to_xml
from fasthtml_extn.libraries.tailwind import ExtnHtml
from fasthtml_extn.utils import create_metacall_app, get_metacall_app_path

pages = create_metacall_app()


def _with_route(path: str):
    def app():
        p = path
        if not p.startswith("/"):
            p = f"/{p}"
        res = get_metacall_app_path(p, pages)
        return to_xml(ExtnHtml(res))

    return app


def deploy_metacall_faas() -> list[str]:
    """
    Discover functions in the module and add them to _all_
    """
    frame = inspect.currentframe()
    if frame is None:
        raise RuntimeError(
            "Cannot deploy functions in the module. Please call this function from a module."
        )
    caller_frame = frame.f_back
    caller_module = inspect.getmodule(caller_frame)

    _all_ = []
    for page in pages:
        app = pages[page]
        route = app["route"]
        function_name = f"app{route}"
        print("Adding Function", function_name)
        setattr(caller_module, function_name, _with_route(route))
        if function_name not in _all_:
            _all_.append(function_name)
    if "app" not in _all_:
        setattr(caller_module, "app", _with_route(""))
        _all_.append("app")
    return _all_
