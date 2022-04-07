from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

from ...._utils import send_session_request
from .._ItemBase import ItemBase
from .AddPartParams import AddPartParams
from .AddResourcesParams import AddResourcesParams
from .ShareUserItemParams import ShareUserItemParams
from .UpdateItemParams import UpdateItemParams
from .UpdateResourcesParams import UpdateResourcesParams
from .UserItemStatusParams import UserItemStatusParams


class UserItem(ItemBase):
    @property
    def username(self):
        return self._pdata["username"]

    @property
    def _url_full(self):
        return "{0}/items/{1}".format(self._url_base, self.id)

    def __init__(self, requests_session, content_url, username, item_id):
        super().__init__(requests_session, content_url, item_id)

        self._pdata["username"] = username

    def add_part(self, add_part_params):
        add_part_params = add_part_params._get_params() if isinstance(add_part_params,
                                                                      AddPartParams) else add_part_params
        r = self._create_operation_request(self, "addPart", method="POST", data=add_part_params)
        return send_session_request(self._session, r).json()

    def add_resources(self, add_resources_params):
        add_resources_params = add_resources_params._get_params() if isinstance(
            add_resources_params, AddResourcesParams) else add_resources_params
        r = self._create_operation_request(self, "addResources", method="POST", data=add_resources_params)
        return send_session_request(self._session, r).json()

    def check_status(self, status_request):
        r = self._create_operation_request(self, "status", method="POST", data=status_request)
        return send_session_request(self._session, r).json()

    def commit(self):
        r = self._create_operation_request(self, "commit", method="POST")
        return send_session_request(self._session, r).json()

    def delete(self):
        r = self._create_operation_request(self, "delete", method="POST")
        return send_session_request(self._session, r).json()

    def move(self, folder_id):
        r = self._create_operation_request(self, "move", method="POST", data={"folder": folder_id})
        return send_session_request(self._session, r).json()

    def get_properties(self):
        """
        Gets the properties of the item.
        """
        return self._get()["item"]

    def get_sharing(self):
        """
        Gets the sharing details of the item.
        """
        return self._get().get("sharing")

    def share(self, share_user_item_params):
        share_user_item_params = share_user_item_params._get_params() if isinstance(
            share_user_item_params, ShareUserItemParams) else share_user_item_params

        return super().share(share_user_item_params)

    def status(self, user_item_status_params):
        user_item_status_params = user_item_status_params._get_params() if isinstance(
            user_item_status_params, UserItemStatusParams) else user_item_status_params
        r = self._create_operation_request(self, "status", method="POST", data=user_item_status_params)
        return send_session_request(self._session, r).json()

    def update(self, update_item_params):
        update_item_params = update_item_params._get_params() if isinstance(update_item_params,
                                                                            UpdateItemParams) else update_item_params
        r = self._create_operation_request(self, "update", method="POST", data=update_item_params)
        return send_session_request(self._session, r).json()

    def update_resources(self, update_resources_params):
        update_resources_params = update_resources_params._get_params() if isinstance(
            update_resources_params, UpdateResourcesParams) else update_resources_params
        r = self._create_operation_request(self, "updateResources", method="POST", data=update_resources_params)
        return send_session_request(self._session, r).json()

    def update_thumbnail(self, updated_thumbnail_info):
        r = self._create_operation_request(self, "updateThumbnail", method="POST", data=updated_thumbnail_info)
        return send_session_request(self._session, r).json()