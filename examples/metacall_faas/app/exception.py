from fasthtml.common import Body


def page(*args, **kwargs):
    return Body(
        "Oops! Something went wrong!",
        *args,
        cls="bg-black/90 h-screen",
        **kwargs,
    )
