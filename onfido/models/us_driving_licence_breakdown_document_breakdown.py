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

class UsDrivingLicenceBreakdownDocumentBreakdown(BaseModel):
    """
    UsDrivingLicenceBreakdownDocumentBreakdown
    """ # noqa: E501
    category: Optional[DocumentBreakdownDataComparisonBreakdownIssuingCountry] = None
    expiration_date: Optional[DocumentBreakdownDataComparisonBreakdownIssuingCountry] = None
    issue_date: Optional[DocumentBreakdownDataComparisonBreakdownIssuingCountry] = None
    document_number: Optional[DocumentBreakdownDataComparisonBreakdownIssuingCountry] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["category", "expiration_date", "issue_date", "document_number"]

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
        """Create an instance of UsDrivingLicenceBreakdownDocumentBreakdown from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expiration_date
        if self.expiration_date:
            _dict['expiration_date'] = self.expiration_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issue_date
        if self.issue_date:
            _dict['issue_date'] = self.issue_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_number
        if self.document_number:
            _dict['document_number'] = self.document_number.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsDrivingLicenceBreakdownDocumentBreakdown from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": DocumentBreakdownDataComparisonBreakdownIssuingCountry.from_dict(obj["category"]) if obj.get("category") is not None else None,
            "expiration_date": DocumentBreakdownDataComparisonBreakdownIssuingCountry.from_dict(obj["expiration_date"]) if obj.get("expiration_date") is not None else None,
            "issue_date": DocumentBreakdownDataComparisonBreakdownIssuingCountry.from_dict(obj["issue_date"]) if obj.get("issue_date") is not None else None,
            "document_number": DocumentBreakdownDataComparisonBreakdownIssuingCountry.from_dict(obj["document_number"]) if obj.get("document_number") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


