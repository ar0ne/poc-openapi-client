import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.author import Author


T = TypeVar("T", bound="Book")


@_attrs_define
class Book:
    """Book model serializer

    Attributes:
        authors (List['Author']):
        content (str):
        created (datetime.datetime):
        id (str):
        title (str):
    """

    authors: List["Author"]
    content: str
    created: datetime.datetime
    id: str
    title: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authors = []
        for authors_item_data in self.authors:
            authors_item = authors_item_data.to_dict()

            authors.append(authors_item)

        content = self.content
        created = self.created.isoformat()

        id = self.id
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authors": authors,
                "content": content,
                "created": created,
                "id": id,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.author import Author

        d = src_dict.copy()
        authors = []
        _authors = d.pop("authors")
        for authors_item_data in _authors:
            authors_item = Author.from_dict(authors_item_data)

            authors.append(authors_item)

        content = d.pop("content")

        created = isoparse(d.pop("created"))

        id = d.pop("id")

        title = d.pop("title")

        book = cls(
            authors=authors,
            content=content,
            created=created,
            id=id,
            title=title,
        )

        book.additional_properties = d
        return book

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
