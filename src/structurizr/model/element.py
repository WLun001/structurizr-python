# Copyright (c) 2020, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Provide a superclass for all model elements."""


from abc import ABC
from typing import Any, ClassVar, Set

from pydantic import Field, HttpUrl

from .model_item import ModelItem


__all__ = ("Element",)


class Element(ModelItem, ABC):
    """
    Define a superclass for all model elements.

    Attributes:
        name (str):
        description (str):
        url (pydantic.HttpUrl):
        relationships (set of Relationship):

    """

    # model: Model
    name: str = Field(...)
    description: str = ""
    url: HttpUrl = ""
    relationships: Set[Any] = set()

    CANONICAL_NAME_SEPARATOR: ClassVar[str] = "/"
