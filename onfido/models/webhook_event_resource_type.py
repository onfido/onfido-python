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


class WebhookEventResourceType(str, Enum):
    """
    WebhookEventResourceType
    """

    """
    allowed enum values
    """
    CHECK = 'check'
    REPORT = 'report'
    AUDIT_LOG = 'audit_log'
    WORKFLOW_RUN = 'workflow_run'
    WORKFLOW_TASK = 'workflow_task'
    WATCHLIST_MONITOR = 'watchlist_monitor'
    WORKFLOW_TIMELINE_FILE = 'workflow_timeline_file'
    WORKFLOW_RUN_EVIDENCE_FOLDER = 'workflow_run_evidence_folder'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WebhookEventResourceType from a JSON string"""
        return cls(json.loads(json_str))


