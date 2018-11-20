# -*- coding: utf-8 -*-
"""
transistor.persistence.containers
~~~~~~~~~~~~
This module contains classes which inherit from class:Item, they encapsulate
data returned from a SplashScraper object after a scrape.  This provides
common output data format, useful for further processing, like serialization,
as needed. For example, enable the data to be pickled and saved in newt.db.

Any changes to this module should also be checked against the ScrapedDataExporter
in the exporter.py file. The attributes here must match up to the
ScrapedDataExporter.write method.

:copyright: Copyright (C) 2018 by BOM Quote Limited
:license: The MIT License, see LICENSE for more details.
~~~~~~~~~~~~
"""

from transistor.persistence.item import Item, Field


class SplashScraperItems(Item):
    """
    A base class which should be inherited in a subclass which then implements
    a customized SplashScraperContainer instance.
    """

    # -- the Scraper's browser class -> self.browser data -- #

    # self.browser.raw_content
    raw_content = Field()
    # this is the status code received from splash (NOT THE ENDPOINT)
    # self.browser.status
    status = Field()
    # self.browser.get_current_request() -> <PreparedRequest [POST]>
    current_request = Field()
    # self.browser.get_current_url() -> 'http://localhost:8050/execute'
    current_url = Field()
    # flag for a python-request timeout error which should mean there was
    # some network problem or reason second number in the timeout tuple like
    # (3.0, 700.0)  was not long enough.
    timeout_exception = Field()

    encoding = Field()
    ucontent = Field()
    resp_content = Field()
    resp_content_type_header = Field()
    resp_headers = Field()
    har = Field()
    png = Field()
    endpoint_status = Field()
    crawlera_session = Field()
    html = Field()

    # /end self.browser

    # -- splash scraper class attributes -- #

    # get the __repr__()
    scraper_repr = Field()
    name = Field()
    number = Field()  # str() or int(), `number` is used to enumerate individual workers
    # the specially prepared self.cookies which would need set by us
    cookies = Field()
    splash_args = Field()
    http_session_valid = Field()
    baseurl = Field()
    crawlera_user = Field()
    referrer = Field()
    searchurl = Field()
    LUA_SOURCE = Field()
    _test_true = Field()
    _result = Field()