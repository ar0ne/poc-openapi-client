from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import Unset

T = TypeVar("T", bound="BookRequest")


@_attrs_define
class BookRequest:
    """Book model serializer

    Attributes:
        content (str):
        title (str):
    """

    content: str
    title: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "title": title,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        content = self.content if isinstance(self.content, Unset) else (None, str(self.content).encode(), "text/plain")
        title = self.title if isinstance(self.title, Unset) else (None, str(self.title).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "content": content,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        title = d.pop("title")

        book_request = cls(
            content=content,
            title=title,
        )

        book_request.additional_properties = d
        return book_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
