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
from onfido.models.document_breakdown_visual_authenticity_breakdown_digital_tampering import DocumentBreakdownVisualAuthenticityBreakdownDigitalTampering
from onfido.models.document_breakdown_visual_authenticity_breakdown_face_detection import DocumentBreakdownVisualAuthenticityBreakdownFaceDetection
from onfido.models.document_breakdown_visual_authenticity_breakdown_fonts import DocumentBreakdownVisualAuthenticityBreakdownFonts
from onfido.models.document_breakdown_visual_authenticity_breakdown_original_document_present import DocumentBreakdownVisualAuthenticityBreakdownOriginalDocumentPresent
from onfido.models.document_breakdown_visual_authenticity_breakdown_other import DocumentBreakdownVisualAuthenticityBreakdownOther
from onfido.models.document_breakdown_visual_authenticity_breakdown_picture_face_integrity import DocumentBreakdownVisualAuthenticityBreakdownPictureFaceIntegrity
from onfido.models.document_breakdown_visual_authenticity_breakdown_security_features import DocumentBreakdownVisualAuthenticityBreakdownSecurityFeatures
from onfido.models.document_breakdown_visual_authenticity_breakdown_template import DocumentBreakdownVisualAuthenticityBreakdownTemplate
from typing import Optional, Set
from typing_extensions import Self

class DocumentBreakdownVisualAuthenticityBreakdown(BaseModel):
    """
    DocumentBreakdownVisualAuthenticityBreakdown
    """ # noqa: E501
    fonts: Optional[DocumentBreakdownVisualAuthenticityBreakdownFonts] = None
    picture_face_integrity: Optional[DocumentBreakdownVisualAuthenticityBreakdownPictureFaceIntegrity] = None
    template: Optional[DocumentBreakdownVisualAuthenticityBreakdownTemplate] = None
    security_features: Optional[DocumentBreakdownVisualAuthenticityBreakdownSecurityFeatures] = None
    original_document_present: Optional[DocumentBreakdownVisualAuthenticityBreakdownOriginalDocumentPresent] = None
    digital_tampering: Optional[DocumentBreakdownVisualAuthenticityBreakdownDigitalTampering] = None
    other: Optional[DocumentBreakdownVisualAuthenticityBreakdownOther] = None
    face_detection: Optional[DocumentBreakdownVisualAuthenticityBreakdownFaceDetection] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["fonts", "picture_face_integrity", "template", "security_features", "original_document_present", "digital_tampering", "other", "face_detection"]

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
        """Create an instance of DocumentBreakdownVisualAuthenticityBreakdown from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fonts
        if self.fonts:
            _dict['fonts'] = self.fonts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of picture_face_integrity
        if self.picture_face_integrity:
            _dict['picture_face_integrity'] = self.picture_face_integrity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security_features
        if self.security_features:
            _dict['security_features'] = self.security_features.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_document_present
        if self.original_document_present:
            _dict['original_document_present'] = self.original_document_present.to_dict()
        # override the default output from pydantic by calling `to_dict()` of digital_tampering
        if self.digital_tampering:
            _dict['digital_tampering'] = self.digital_tampering.to_dict()
        # override the default output from pydantic by calling `to_dict()` of other
        if self.other:
            _dict['other'] = self.other.to_dict()
        # override the default output from pydantic by calling `to_dict()` of face_detection
        if self.face_detection:
            _dict['face_detection'] = self.face_detection.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentBreakdownVisualAuthenticityBreakdown from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fonts": DocumentBreakdownVisualAuthenticityBreakdownFonts.from_dict(obj["fonts"]) if obj.get("fonts") is not None else None,
            "picture_face_integrity": DocumentBreakdownVisualAuthenticityBreakdownPictureFaceIntegrity.from_dict(obj["picture_face_integrity"]) if obj.get("picture_face_integrity") is not None else None,
            "template": DocumentBreakdownVisualAuthenticityBreakdownTemplate.from_dict(obj["template"]) if obj.get("template") is not None else None,
            "security_features": DocumentBreakdownVisualAuthenticityBreakdownSecurityFeatures.from_dict(obj["security_features"]) if obj.get("security_features") is not None else None,
            "original_document_present": DocumentBreakdownVisualAuthenticityBreakdownOriginalDocumentPresent.from_dict(obj["original_document_present"]) if obj.get("original_document_present") is not None else None,
            "digital_tampering": DocumentBreakdownVisualAuthenticityBreakdownDigitalTampering.from_dict(obj["digital_tampering"]) if obj.get("digital_tampering") is not None else None,
            "other": DocumentBreakdownVisualAuthenticityBreakdownOther.from_dict(obj["other"]) if obj.get("other") is not None else None,
            "face_detection": DocumentBreakdownVisualAuthenticityBreakdownFaceDetection.from_dict(obj["face_detection"]) if obj.get("face_detection") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


