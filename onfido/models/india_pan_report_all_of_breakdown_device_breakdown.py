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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from onfido.models.india_pan_report_all_of_breakdown_device_breakdown_pan_valid import IndiaPanReportAllOfBreakdownDeviceBreakdownPanValid
from typing import Optional, Set
from typing_extensions import Self

class IndiaPanReportAllOfBreakdownDeviceBreakdown(BaseModel):
    """
    IndiaPanReportAllOfBreakdownDeviceBreakdown
    """ # noqa: E501
    pan_valid: Optional[IndiaPanReportAllOfBreakdownDeviceBreakdownPanValid] = None
    name_match: Optional[IndiaPanReportAllOfBreakdownDeviceBreakdownPanValid] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["pan_valid", "name_match"]

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
        """Create an instance of IndiaPanReportAllOfBreakdownDeviceBreakdown from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pan_valid
        if self.pan_valid:
            _dict['pan_valid'] = self.pan_valid.to_dict()
        # override the default output from pydantic by calling `to_dict()` of name_match
        if self.name_match:
            _dict['name_match'] = self.name_match.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndiaPanReportAllOfBreakdownDeviceBreakdown from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pan_valid": IndiaPanReportAllOfBreakdownDeviceBreakdownPanValid.from_dict(obj["pan_valid"]) if obj.get("pan_valid") is not None else None,
            "name_match": IndiaPanReportAllOfBreakdownDeviceBreakdownPanValid.from_dict(obj["name_match"]) if obj.get("name_match") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


