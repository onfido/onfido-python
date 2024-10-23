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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from onfido.models.address_builder import AddressBuilder
from onfido.models.applicant_consent_builder import ApplicantConsentBuilder
from onfido.models.id_number import IdNumber
from onfido.models.location_builder import LocationBuilder
from typing import Optional, Set
from typing_extensions import Self

class ApplicantUpdater(BaseModel):
    """
    ApplicantUpdater
    """ # noqa: E501
    email: Optional[StrictStr] = Field(default=None, description="The applicant's email address. Required if doing a US check, or a UK check for which `applicant_provides_data` is `true`.")
    dob: Optional[date] = Field(default=None, description="The applicant's date of birth")
    id_numbers: Optional[List[IdNumber]] = None
    phone_number: Optional[StrictStr] = Field(default=None, description="The applicant's phone number")
    consents: Optional[List[ApplicantConsentBuilder]] = Field(default=None, description="The applicant's consents")
    address: Optional[AddressBuilder] = None
    location: Optional[LocationBuilder] = None
    first_name: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The applicant's first name")
    last_name: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The applicant's surname")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["email", "dob", "id_numbers", "phone_number", "consents", "address", "location", "first_name", "last_name"]

    @field_validator('first_name')
    def first_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[^!#$%*=<>;{}\"]*$", value):
            raise ValueError(r"must validate the regular expression /^[^!#$%*=<>;{}\"]*$/")
        return value

    @field_validator('last_name')
    def last_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[^!#$%*=<>;{}\"]*$", value):
            raise ValueError(r"must validate the regular expression /^[^!#$%*=<>;{}\"]*$/")
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
        """Create an instance of ApplicantUpdater from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in id_numbers (list)
        _items = []
        if self.id_numbers:
            for _item_id_numbers in self.id_numbers:
                if _item_id_numbers:
                    _items.append(_item_id_numbers.to_dict())
            _dict['id_numbers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in consents (list)
        _items = []
        if self.consents:
            for _item_consents in self.consents:
                if _item_consents:
                    _items.append(_item_consents.to_dict())
            _dict['consents'] = _items
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicantUpdater from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "dob": obj.get("dob"),
            "id_numbers": [IdNumber.from_dict(_item) for _item in obj["id_numbers"]] if obj.get("id_numbers") is not None else None,
            "phone_number": obj.get("phone_number"),
            "consents": [ApplicantConsentBuilder.from_dict(_item) for _item in obj["consents"]] if obj.get("consents") is not None else None,
            "address": AddressBuilder.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "location": LocationBuilder.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


