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
from onfido.models.document_breakdown_data_comparison_breakdown_issuing_country import DocumentBreakdownDataComparisonBreakdownIssuingCountry
from typing import Optional, Set
from typing_extensions import Self

class UsDrivingLicenceBreakdownAddressBreakdown(BaseModel):
    """
    UsDrivingLicenceBreakdownAddressBreakdown
    """ # noqa: E501
    city: Optional[DocumentBreakdownDataComparisonBreakdownIssuingCountry] = None
    line_1: Optional[DocumentBreakdownDataComparisonBreakdownIssuingCountry] = None
    line_2: Optional[DocumentBreakdownDataComparisonBreakdownIssuingCountry] = None
    state_code: Optional[DocumentBreakdownDataComparisonBreakdownIssuingCountry] = None
    zip4: Optional[DocumentBreakdownDataComparisonBreakdownIssuingCountry] = None
    zip5: Optional[DocumentBreakdownDataComparisonBreakdownIssuingCountry] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["city", "line_1", "line_2", "state_code", "zip4", "zip5"]

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
        """Create an instance of UsDrivingLicenceBreakdownAddressBreakdown from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of city
        if self.city:
            _dict['city'] = self.city.to_dict()
        # override the default output from pydantic by calling `to_dict()` of line_1
        if self.line_1:
            _dict['line_1'] = self.line_1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of line_2
        if self.line_2:
            _dict['line_2'] = self.line_2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state_code
        if self.state_code:
            _dict['state_code'] = self.state_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of zip4
        if self.zip4:
            _dict['zip4'] = self.zip4.to_dict()
        # override the default output from pydantic by calling `to_dict()` of zip5
        if self.zip5:
            _dict['zip5'] = self.zip5.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsDrivingLicenceBreakdownAddressBreakdown from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "city": DocumentBreakdownDataComparisonBreakdownIssuingCountry.from_dict(obj["city"]) if obj.get("city") is not None else None,
            "line_1": DocumentBreakdownDataComparisonBreakdownIssuingCountry.from_dict(obj["line_1"]) if obj.get("line_1") is not None else None,
            "line_2": DocumentBreakdownDataComparisonBreakdownIssuingCountry.from_dict(obj["line_2"]) if obj.get("line_2") is not None else None,
            "state_code": DocumentBreakdownDataComparisonBreakdownIssuingCountry.from_dict(obj["state_code"]) if obj.get("state_code") is not None else None,
            "zip4": DocumentBreakdownDataComparisonBreakdownIssuingCountry.from_dict(obj["zip4"]) if obj.get("zip4") is not None else None,
            "zip5": DocumentBreakdownDataComparisonBreakdownIssuingCountry.from_dict(obj["zip5"]) if obj.get("zip5") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

