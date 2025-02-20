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


class WebhookEventType(str, Enum):
    """
    WebhookEventType
    """

    """
    allowed enum values
    """
    AUDIT_LOG_DOT_CREATED = 'audit_log.created'
    WATCHLIST_MONITOR_DOT_MATCHES_UPDATED = 'watchlist_monitor.matches_updated'
    WORKFLOW_RUN_DOT_COMPLETED = 'workflow_run.completed'
    WORKFLOW_TASK_DOT_STARTED = 'workflow_task.started'
    WORKFLOW_TASK_DOT_COMPLETED = 'workflow_task.completed'
    CHECK_DOT_STARTED = 'check.started'
    CHECK_DOT_REOPENED = 'check.reopened'
    CHECK_DOT_WITHDRAWN = 'check.withdrawn'
    CHECK_DOT_COMPLETED = 'check.completed'
    CHECK_DOT_FORM_COMPLETED = 'check.form_completed'
    REPORT_DOT_WITHDRAWN = 'report.withdrawn'
    REPORT_DOT_RESUMED = 'report.resumed'
    REPORT_DOT_CANCELLED = 'report.cancelled'
    REPORT_DOT_AWAITING_APPROVAL = 'report.awaiting_approval'
    REPORT_DOT_COMPLETED = 'report.completed'
    WORKFLOW_TIMELINE_FILE_DOT_CREATED = 'workflow_timeline_file.created'
    WORKFLOW_RUN_EVIDENCE_FOLDER_DOT_CREATED = 'workflow_run_evidence_folder.created'
    UNKNOWN_DEFAULT_OPEN_API = 'unknown_default_open_api'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WebhookEventType from a JSON string"""
        return cls(json.loads(json_str))


