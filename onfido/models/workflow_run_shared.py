# coding: utf-8

"""
    Onfido API v3.6

    The Onfido API (v3.6)

    The version of the OpenAPI document: v3.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from onfido.models.workflow_run_link import WorkflowRunLink
from typing import Optional, Set
from typing_extensions import Self

class WorkflowRunShared(BaseModel):
    """
    WorkflowRunShared
    """ # noqa: E501
    applicant_id: StrictStr = Field(description="The unique identifier for the Applicant.")
    workflow_id: StrictStr = Field(description="The unique identifier for the Workflow.")
    tags: Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True, max_length=128)]], Field(max_length=30)]] = Field(default=None, description="Tags or labels assigned to the workflow run.")
    customer_user_id: Optional[Annotated[str, Field(strict=True, max_length=256)]] = Field(default=None, description="Customer-provided user identifier.")
    link: Optional[WorkflowRunLink] = Field(default=None, description="Object for the configuration of the Workflow Run link.")
    created_at: Optional[datetime] = Field(default=None, description="The date and time when the Workflow Run was created.")
    updated_at: Optional[datetime] = Field(default=None, description="The date and time when the Workflow Run was last updated.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["applicant_id", "workflow_id", "tags", "customer_user_id", "link", "created_at", "updated_at"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WorkflowRunShared from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of link
        if self.link:
            _dict['link'] = self.link.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkflowRunShared from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "applicant_id": obj.get("applicant_id"),
            "workflow_id": obj.get("workflow_id"),
            "tags": obj.get("tags"),
            "customer_user_id": obj.get("customer_user_id"),
            "link": WorkflowRunLink.from_dict(obj["link"]) if obj.get("link") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


