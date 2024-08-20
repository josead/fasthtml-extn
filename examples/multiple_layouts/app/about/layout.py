from fasthtml.common import Div


def layout(*args, **kwargs):
    return Div(
        *args,
        cls="p-20 bg-teal-300 rounded-lg shadow-sm h-screen flex flex-col justify-center items-center",
        **kwargs,
    )
