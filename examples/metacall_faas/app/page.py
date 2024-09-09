from fasthtml.common import Title, Div, A


def page(context):
    return Div(
        Title("Hello there!"),
        A(
            "Go to Counter",
            href="app/counter",
            cls="text-blue-500 p-5 bg-white/5 hover:bg-white/10 rounded-lg",
        ),
        A(
            "Go to About",
            href="app/about/me",
            cls="text-blue-500 p-5 bg-white/5 hover:bg-white/10 rounded-lg",
        ),
        A(
            "Go to About Project",
            href="app/about/project",
            cls="text-blue-500 p-5 bg-white/5 hover:bg-white/10 rounded-lg",
        ),
        cls="flex flex-col h-screen justify-center items-center",
    )
