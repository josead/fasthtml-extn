from fasthtml.common import Div

from fasthtml_extn.libraries.tailwind import (
    ExtnContainer,
    ExtnHtml,
    ExtnContent,
    ExtnHtml,
)


def layout(*args, **kwargs):
    return ExtnHtml(
        Div(
            ExtnContainer(
                ExtnContent(
                    *args,
                    **kwargs,
                ),
            ),
            cls="bg-black/90 h-screen",
        )
    )
