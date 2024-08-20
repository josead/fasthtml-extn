from fasthtml.common import Div


def layout(*args, **kwargs):
    return Div(
        *args,
        cls="p-20 bg-red-400/60 rounded-lg shadow-sm",
        **kwargs,
    )
