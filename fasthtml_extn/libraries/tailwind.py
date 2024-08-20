from fasthtml.common import Div, Html, Button, Script
from fasthtml.common import Script, Style

htmx_link = Script(src="https://unpkg.com/htmx.org@next/dist/htmx.min.js")
plugins = "forms,typography,aspect-ratio,container-queries"
tailwind_link = (
    Script(src=f"https://cdn.tailwindcss.com?plugins={plugins}"),
    Style(
        """
@layer utilities {
      .content-auto {
        content-visibility: auto;
      }
    }""",
        type="text/tailwindcss",
    ),
)


def ExtnHtml(*args, **kwargs):
    # When you use Html, you have to add htmx (which is optional, but necessary for using hx_ attributes)
    return Html(
        htmx_link,
        tailwind_link,
        *args,
        **kwargs,
    )


# Some Components using tailwindcss


def ExtnContainer(*args, **kwargs):
    return Div(*args, cls=f"mx-auto max-w-7xl sm:px-4 lg:px-8", **kwargs)


def ExtnContent(*args, **kwargs):
    return Div(
        Div(*args, cls="mx-auto max-w-3xl"),
        cls="mx-auto max-w-7xl px-4 sm:px-4 lg:px-8",
        **kwargs,
    )


def ExtnCard(*args, header, footer, **kwargs):
    return Div(
        Div(header, cls="px-4 py-5 sm:px-4"),
        Div(*args, cls="px-4 py-5 sm:p-6"),
        Div(footer, cls="px-4 py-4 sm:px-4"),
        cls="divide-y divide-gray-200 overflow-hidden rounded-lg bg-white shadow",
        **kwargs,
    )


def ExtnButton(*args, **kwargs):
    return Button(
        *args,
        cls="rounded-full bg-teal-600 p-1 text-white shadow-sm hover:bg-teal-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-teal-600",
        **kwargs,
    )
