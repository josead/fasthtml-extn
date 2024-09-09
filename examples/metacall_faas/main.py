import logging
from fasthtml_extn.deploy import render_fasthtml_factory
from fasthtml_extn.utils import create_metacall_app

logging.basicConfig(level=logging.INFO)
logging.getLogger("fasthtml_extn_metacall").setLevel(logging.INFO)

# Initialize __all__ as an empty list
__all__ = []

pages = create_metacall_app()


def deploy_metacall_faas():
    """
    Discover functions in the module and add them to __all__
    """

    for page in pages:
        app = pages[page]
        route = app["route"]
        function_name = f"app{route}"
        logging.info(f"Adding Function {function_name}")
        globals()[function_name] = render_fasthtml_factory(route, pages)
        if function_name not in __all__:
            __all__.append(function_name)
    if "app" not in __all__:
        globals()["app"] = render_fasthtml_factory("", pages)
        __all__.append("app")
