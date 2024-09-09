import logging

logger = logging.getLogger("app_logger")


from fasthtml.common import P, Div
from fasthtml_extn.libraries.icons import (
    PlusIcon,
    RotateCCW,
)

from fasthtml_extn.libraries.tailwind import (
    ExtnButton,
    ExtnCard,
)


class CounterState:
    def __init__(self):
        self.count = 0

    def increment(self):
        logger.info("incrementing")
        self.count += 1
        return self.count

    def reset(self):
        logger.info("resetting")
        self.count = 0
        return self.count


counter_state = CounterState()


def page(context=None):

    return Div(
        ExtnCard(
            P(f"{counter_state.count}", id="count"),
            header=P("Counter App", cls="text-lg font-semibold"),
            footer=Div(
                P(
                    "Click the + button to increment the counter, and the [back] button to reset it.",
                    cls="w-40",
                ),
                Div(
                    ExtnButton(
                        PlusIcon(cls="bg-white w-5 h-5"),
                        hx_post=counter_state.increment,
                        hx_target="#count",
                        hx_swap="textContent",
                    ),
                    ExtnButton(
                        RotateCCW(cls="bg-white w-5 h-5"),
                        hx_post=counter_state.reset,
                        hx_target="#count",
                        hx_swap="textContent",
                    ),
                ),
                cls="flex justify-between",
            ),
        ),
        cls="h-screen flex justify-center items-center",
    )
