from fasthtml.core import to_xml

from fasthtml_extn.libraries.tailwind import ExtnHtml
from fasthtml_extn.utils import create_metacall_app, get_metacall_app_path


pages = create_metacall_app()


def app(*args, **kwargs):

    # example of possible args = ("dashboard", "partners", "id_4782348")
    # each argument represents a different page

    path = "/" + "/".join(args)

    res = get_metacall_app_path(path, pages)

    return to_xml(ExtnHtml(res))
