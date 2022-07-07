from typing import Optional

from selene import have
from selene.support.shared import browser


def tags_input(element, from_: str, /, *, autocomplete: Optional[str] = None):
    if autocomplete:
        element.type(from_)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(autocomplete)).click()
    else:
        element.type(from_).press_tab()
