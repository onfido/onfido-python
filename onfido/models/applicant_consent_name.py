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


class ApplicantConsentName(str, Enum):
    """
    ApplicantConsentName
    """

    """
    allowed enum values
    """
    PRIVACY_NOTICES_READ = 'privacy_notices_read'
    SSN_VERIFICATION = 'ssn_verification'
    PHONE_NUMBER_VERIFICATION = 'phone_number_verification'
    UNKNOWN_DEFAULT_OPEN_API = 'unknown_default_open_api'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApplicantConsentName from a JSON string"""
        return cls(json.loads(json_str))


