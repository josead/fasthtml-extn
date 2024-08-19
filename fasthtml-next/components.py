from functools import partial
from fasthtml.common import Div, Html, Button, Script, Img
from tailwind import tailwind_link

htmx_link = Script(src="https://unpkg.com/htmx.org@next/dist/htmx.min.js")


def TWHtml(*args, **kwargs):
    # When you use Html, you have to add htmx (which is optional, but necessary for using hx_ attributes)
    return Html(
        htmx_link,
        tailwind_link,
        *args,
        **kwargs,
    )


# Some TW Components


def TWContainer(*args, **kwargs):
    return Div(*args, cls=f"mx-auto max-w-7xl sm:px-4 lg:px-8", **kwargs)


def TWContent(*args, **kwargs):
    return Div(
        Div(*args, cls="mx-auto max-w-3xl"),
        cls="mx-auto max-w-7xl px-4 sm:px-4 lg:px-8",
        **kwargs,
    )


def TWCard(*args, header, footer, **kwargs):
    return Div(
        Div(header, cls="px-4 py-5 sm:px-4"),
        Div(*args, cls="px-4 py-5 sm:p-6"),
        Div(footer, cls="px-4 py-4 sm:px-4"),
        cls="divide-y divide-gray-200 overflow-hidden rounded-lg bg-white shadow",
        **kwargs,
    )


def TWButton(*args, **kwargs):
    return Button(
        *args,
        cls="rounded-full bg-teal-600 p-1 text-white shadow-sm hover:bg-teal-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-teal-600",
        **kwargs,
    )


# Icons


def ImgIcon(*args, url, **kwargs):
    return Img(
        *args,
        style=f'mask-image: url("{url}"); mask-size: auto 100%; mask-repeat: no-repeat;',
        **kwargs,
    )


RotateCCW = partial(
    ImgIcon,
    url="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLXJvdGF0ZS1jY3ciPjxwYXRoIGQ9Ik0zIDEyYTkgOSAwIDEgMCA5LTkgOS43NSA5Ljc1IDAgMCAwLTYuNzQgMi43NEwzIDgiLz48cGF0aCBkPSJNMyAzdjVoNSIvPjwvc3ZnPg==",
)
PlusIcon = partial(
    ImgIcon,
    url="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLXBsdXMiPjxwYXRoIGQ9Ik01IDEyaDE0Ii8+PHBhdGggZD0iTTEyIDV2MTQiLz48L3N2Zz4=",
)


# Layouts


def NotFound(context):
    return TWContent(
        TWCard(
            TWContainer(
                "Not Found",
            ),
            header="404",
            footer="The page you are looking for does not exist.",
        ),
    )
