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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from onfido.models.country_codes import CountryCodes
from typing import Optional, Set
from typing_extensions import Self

class Document(BaseModel):
    """
    Document
    """ # noqa: E501
    file_type: Optional[StrictStr] = Field(default=None, description="The file type of the uploaded file")
    type: Optional[StrictStr] = Field(default=None, description="The type of document")
    side: Optional[StrictStr] = Field(default=None, description="The side of the document, if applicable. The possible values are front and back")
    issuing_country: Optional[CountryCodes] = Field(default=None, description="The issuing country of the document, a 3-letter ISO code.")
    applicant_id: Optional[StrictStr] = Field(default=None, description="The ID of the applicant whose document is being uploaded.")
    id: StrictStr = Field(description="The unique identifier for the document")
    created_at: Optional[datetime] = Field(default=None, description="The date and time at which the document was uploaded")
    href: Optional[StrictStr] = Field(default=None, description="The uri of this resource")
    download_href: Optional[StrictStr] = Field(default=None, description="The uri that can be used to download the document")
    file_name: Optional[StrictStr] = Field(default=None, description="The name of the uploaded file")
    file_size: Optional[StrictInt] = Field(default=None, description="The size of the file in bytes")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["file_type", "type", "side", "issuing_country", "applicant_id", "id", "created_at", "href", "download_href", "file_name", "file_size"]

    @field_validator('file_type')
    def file_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['jpg', 'jpeg', 'png', 'pdf']):
            raise ValueError("must be one of enum values ('jpg', 'jpeg', 'png', 'pdf')")
        return value

    @field_validator('side')
    def side_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['front', 'back']):
            raise ValueError("must be one of enum values ('front', 'back')")
        return value

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
        """Create an instance of Document from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Document from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "file_type": obj.get("file_type"),
            "type": obj.get("type"),
            "side": obj.get("side"),
            "issuing_country": obj.get("issuing_country"),
            "applicant_id": obj.get("applicant_id"),
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "href": obj.get("href"),
            "download_href": obj.get("download_href"),
            "file_name": obj.get("file_name"),
            "file_size": obj.get("file_size")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


