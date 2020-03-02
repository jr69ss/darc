# -*- coding: utf-8 -*-
"""Requests wrapper."""
# pylint: disable=unused-wildcard-import

import requests
import requests_futures.sessions

import darc.typing as typing
from darc.const import DARC_CPU
from darc.error import UnsupportedLink
from darc.link import Link
from darc.proxy.i2p import I2P_REQUESTS_PROXY
from darc.proxy.tor import TOR_REQUESTS_PROXY


def request_session(link: Link, futures: bool = False) -> typing.Union[typing.Session, typing.FutureSession]:
    """Get requests session."""
    from darc.proxy import LINK_MAP  # pylint: disable=import-outside-toplevel

    session, _ = LINK_MAP[link.proxy]
    if session is None:
        raise UnsupportedLink(link.url)
    return session(futures=futures)


def i2p_session(futures: bool = False) -> typing.Union[typing.Session, typing.FutureSession]:
    """I2P (.i2p) session."""
    if futures:
        session = requests_futures.sessions.FuturesSession(max_workers=DARC_CPU)
    else:
        session = requests.Session()
    session.proxies.update(I2P_REQUESTS_PROXY)
    return session


def tor_session(futures: bool = False) -> typing.Union[typing.Session, typing.FutureSession]:
    """Tor (.onion) session."""
    if futures:
        session = requests_futures.sessions.FuturesSession(max_workers=DARC_CPU)
    else:
        session = requests.Session()
    session.proxies.update(TOR_REQUESTS_PROXY)
    return session


def null_session(futures: bool = False) -> typing.Union[typing.Session, typing.FutureSession]:
    """Normal session"""
    if futures:
        session = requests_futures.sessions.FuturesSession(max_workers=DARC_CPU)
    else:
        session = requests.Session()
    return session
