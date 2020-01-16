# -*- coding: utf-8 -*-
"""Custom exceptions."""

import stem

import darc.typing as typing


class UnsupportedLink(Exception):
    """The link is not supported."""


class UnsupportedPlatform(Exception):
    """The platform is not supported."""


class TorBootstrapFailed(Warning):
    """Tor bootstrap process failed."""


def render_error(message: str, colour: typing.Color) -> str:
    """Render error message."""
    return ''.join(
        stem.util.term.format(line, colour) for line in message.splitlines(True)
    )
