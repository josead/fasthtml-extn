import sys
import os
import logging
from functools import reduce

from .components import NotFoundPage

logger = logging.getLogger("fasthtml_extn")


def get_path_and_route(
    directory,
    app_dir,
):
    relative_path = os.path.relpath(directory, app_dir)
    if relative_path == ".":
        relative_path = ""

    route = "/" + relative_path.replace(os.sep, "/")
    if route == "/app":
        route = "/"
    return relative_path, route


def get_module(
    relative_path,
    module_name,
):
    if not relative_path:  # If the file is in the root of the app directory
        module_path = f"app.{module_name}"
    else:
        module_path = ".".join(["app"] + relative_path.split(os.sep) + [module_name])
    try:
        return __import__(module_path, fromlist=[module_name])
    except ModuleNotFoundError:
        logger.debug(f"Warning: module_path: '{module_path}' does not exist")
        return None


# This function can be improved, as this is a naive implementation
def collect_layouts(
    directory,
    app_dir,
):
    layouts = []
    current_dir = directory
    while os.path.commonpath([current_dir, app_dir]) == app_dir:
        relative_path = os.path.relpath(current_dir, app_dir)
        if relative_path == ".":
            relative_path = ""
        layout_module = get_module(relative_path, "layout")
        if layout_module and hasattr(layout_module, "layout"):
            layouts.append(getattr(layout_module, "layout"))
        elif layout_module:
            logger.warn(f"Warning: {layout_module} does not have a 'layout' function.")
        current_dir = os.path.dirname(current_dir)
    return layouts


def collect_feature_module(
    directory,
    app_dir,
    feature_name,
):
    current_dir = directory
    while os.path.commonpath([current_dir, app_dir]) == app_dir:
        relative_path = os.path.relpath(current_dir, app_dir)
        if relative_path == ".":
            relative_path = ""
        feature_module_module = get_module(relative_path, feature_name)
        if feature_module_module:
            return feature_module_module
        current_dir = os.path.dirname(current_dir)
    return NotFoundPage


# Modify the register_module_page function
def register_module_page_layouts(
    module,
    route,
    context,
    relative_path,
    layouts,
    not_found,
    _except,
):
    try:
        _, rt = context

        page_init = getattr(module, "page")

        @rt(route, name=route)
        async def get():  # type: ignore
            try:
                content = page_init(context)
                return apply_layouts(content, layouts)
            except Exception as e:
                logger.error(f"Error: /{relative_path} has an error: {e}")
                return _except.error(e, context)

        @rt("{}/{}".format(route, "{path:path}"), name=f"{route}_and_not_found")
        async def get(path: str):
            try:
                content = not_found.page(context)
                return apply_layouts(content, layouts)
            except Exception as e:
                logger.error(f"Error: /{relative_path} has an error: {e}")
                return _except.page(context)

        logger.info(f"Created route: {route}")
    except AttributeError as e:
        logger.warn(f"Warning: {module} does not have a 'page' function.")
    except Exception as e:
        logger.error(f"Error: /{relative_path} has an error: {e}")


# Add this new function to apply layouts
def apply_layouts(
    content,
    layouts,
):
    def nest_layouts(inner_content):
        return reduce(
            lambda inner, outer: lambda: outer(inner()),
            layouts,
            lambda: inner_content,
        )

    return nest_layouts(content)()


# Modify the process_directory function
def process_directory_with_layout(
    directory,
    context,
    base_route="",
    app_dir="",
):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) and item == "page.py":
            relative_path, route = get_path_and_route(directory, app_dir)

            module = get_module(relative_path, "page")
            if module:
                layouts = collect_layouts(directory, app_dir)
                not_found = collect_feature_module(directory, app_dir, "not_found")
                _except = collect_feature_module(directory, app_dir, "except")
                register_module_page_layouts(
                    module,
                    route,
                    context,
                    relative_path,
                    layouts,
                    not_found,
                    _except,
                )
        elif os.path.isdir(item_path) and not item.startswith("__"):
            process_directory_with_layout(
                item_path,
                context,
                os.path.join(base_route, item),
                app_dir=app_dir,
            )


def create_routes(context, app_dir):
    process_directory_with_layout(app_dir, context, app_dir=app_dir)


def get_app_dir():
    startint_dir = os.path.dirname(sys.argv[0])
    current_path = os.path.abspath(startint_dir)
    app_dir = os.path.join(current_path, "app")
    if os.path.isdir(app_dir):
        return app_dir
    else:
        logger.warn("Automation: /app folder does not exist, creating one.")
        os.makedirs(app_dir)
    return app_dir


def create_app(*args, **kwargs):

    app_dir = get_app_dir()
    from fasthtml.common import FastHTMLWithLiveReload, FastHTML

    if kwargs.pop("live", False):
        app = FastHTMLWithLiveReload(*args, **kwargs)
    kwargs.pop("reload_attempts", None)
    kwargs.pop("reload_interval", None)

    app = FastHTML(*args, **kwargs)

    create_routes((app, app.route), app_dir)

    return app, app.route
