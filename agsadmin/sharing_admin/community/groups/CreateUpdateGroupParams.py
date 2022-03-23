from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# standard lib imports
from enum import Enum

# local imports
from ..._ParamsBase import ParamsBase


class GroupAccess(Enum):
    PRIVATE = "private"
    ORD = "org"
    PUBLIC = "public"


class GroupSortField(Enum):
    TITLE = "title"
    OWNER = "owner"
    AVERAGE_RATING = "avgrating"
    NUM_VIEWS = "numviews"
    CREATED = "created"
    MODIFIED = "modified"


class GroupSortOrder(Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


class CreateUpdateGroupParams(ParamsBase):
    """Holds parameter values for the "create" and "update" group functions."""

    @property
    def access(self):
        """Gets or sets the access level for the group."""
        return GroupAccess(self._props.get("access", GroupAccess.PRIVATE))

    @access.setter
    def access(self, value):
        value = GroupAccess(value)
        self._props["access"] = value.value

    @property
    def contact(self):
        """Get or set contact information for the group.
        
        The character limit is 250."""

        # Why if this property called "phone", but can contain any contact information?
        return self._props.get("phone", None)

    @contact.setter
    def contact(self, value):
        if len(value) > 250:
            raise ValueError("Contact information must be no longer than 250 characters.")

        self._props["phone"] = value

    @property
    def description(self):
        """Gets or sets the group description."""
        return self._props.get("description", None)

    @description.setter
    def description(self, value):
        self._props["description"] = value

    @property
    def is_invitation_only(self):
        """Gets or sets a boolean indicating whether the group will accept join requests."""
        return self._props.get("isInvitationOnly", False)

    @is_invitation_only.setter
    def is_invitation_only(self, value):
        value = bool(value)
        self._props["isInvitationOnly"] = value

    @property
    def is_view_only(self):
        """Gets or sets a boolean indicating whether the group is a "view-only" group where members cannot share items."""
        return self._props.get("isViewOnly", False)

    @is_view_only.setter
    def is_view_only(self, value):
        value = bool(value)
        self._props["isViewOnly"] = value

    @property
    def snippet(self):
        """Get or set a short summary of the group.
        
        The character limit is 250."""

        return self._props.get("snippet", None)

    @snippet.setter
    def snippet(self, value):
        if len(value) > 250:
            raise ValueError("Snippet must be no longer than 250 characters.")

        self._props["snippet"] = value

    @property
    def sort_field(self):
        """Gets or sets the sort field for group items."""
        return GroupSortField(self._props.get("sortField", None))

    @sort_field.setter
    def sort_field(self, value):
        value = GroupSortField(value)
        self._props["sortField"] = value.value

    @property
    def sort_order(self):
        """Gets or sets the sort order for group items."""
        return GroupSortOrder(self._props.get("sortOrder", None))

    @sort_order.setter
    def sort_order(self, value):
        value = GroupSortOrder(value)
        self._props["sortOrder"] = value.value

    @property
    def tags(self):
        """Get or set a list of words or short phrases that describe the group."""

        t = self._props.get("tags", None)
        if t == None:
            return []

        return [tag.strip() for tag in t.split(",")]

    @tags.setter
    def tags(self, value):
        self._props = None if value == None else ",".join(value)

    @property
    def thumbnail(self):
        """Gets or sets the path to a thumbnail to use for the group.
        
        The thumbnail will be opened and read at the time a create or update group request is made."""

        return self._props.get("thumbnail", None)

    @thumbnail.setter
    def thumbnail(self, value):
        self._props["thumbnail"] = value

    @property
    def title(self):
        """Gets or sets the title of the group.
        
        The title must be no longer than 250 characters."""

        return self._props.get("title", None)

    @title.setter
    def title(self, value):
        if len(value) > 250:
            raise ValueError("Title must be no longer than 250 characters.")

        self._props["title"] = value
