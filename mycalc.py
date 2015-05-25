#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from .util import (
    union,
    customer_service,
    contract_customer,
    activity_manager,
    directors,
    finance,
    file_auth,
    risk_service_manager,
    superadmin
)

""" Auth map for flask view functions
KEY: <endpoint>
VALUE: <permission groups>
"""
