# coding: utf-8

"""
    Onfido API v3.6

    The Onfido API (v3.6)

    The version of the OpenAPI document: v3.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CheckStatus(str, Enum):
    """
    The current state of the check in the checking process.
    """

    """
    allowed enum values
    """
    IN_PROGRESS = 'in_progress'
    AWAITING_APPLICANT = 'awaiting_applicant'
    COMPLETE = 'complete'
    WITHDRAWN = 'withdrawn'
    PAUSED = 'paused'
    REOPENED = 'reopened'
    UNKNOWN_DEFAULT_OPEN_API = 'unknown_default_open_api'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CheckStatus from a JSON string"""
        return cls(json.loads(json_str))


