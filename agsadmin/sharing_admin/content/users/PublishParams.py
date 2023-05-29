from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# local imports
from ..._ParamsBase import ParamsBase
from .PublishFileType import PublishFileType
from .PublishOutputType import PublishOutputType


class PublishParams(ParamsBase):
    """Holds parameter values for the "publish" user content request."""
    @property
    def build_initial_cache(self):
        """This property is undocumented, but is seen when publishing Vector Tile services."""
        return self._props.get("buildInitialCache")

    @build_initial_cache.setter
    def build_initial_cache(self, value):
        self._set_nullable_bool("buildInitialCache", value)

    @property
    def delete_source_item_upon_completion(self):
        return self._props.get("deleteSourceItemUponCompletion")

    @delete_source_item_upon_completion.setter
    def delete_source_item_upon_completion(self, value):
        self._set_nullable_bool("deleteSourceItemUponCompletion", value)

    @property
    def file(self):
        return self._props.get("file")

    @file.setter
    def file(self, value):
        self._set_nullable("file", value)

    @property
    def file_type(self):
        """Gets or sets the file type to be published."""

        return self._get_nullable_enum("fileType", PublishFileType)

    @file_type.setter
    def file_type(self, value):
        self._set_nullable_enum("fileType", value, PublishFileType)

    @property
    def item_id(self):
        return self._props.get("itemID")

    @item_id.setter
    def item_id(self, value):
        self._set_nullable("itemID", value)

    @property
    def item_id_to_create(self):
        """Gets or sets the item ID of the Portal Item to be published."""
        
        return self._props.get("itemIdToCreate")
    
    @item_id_to_create.setter
    def item_id_to_create(self, value):
        self._set_nullable("itemIdToCreate", value)

    @property
    def output_type(self):
        """Gets or sets the output type of the published service."""

        return self._get_nullable_enum("outputType", PublishOutputType)

    @output_type.setter
    def output_type(self, value):
        self._set_nullable_enum("outputType", value, PublishOutputType)

    @property
    def overwrite(self):
        """Gets or sets the clear empty status value for the request."""
        return self._props.get("overwrite")

    @overwrite.setter
    def overwrite(self, value):
        self._set_nullable_bool("overwrite", value)

    @property
    def publish_parameters(self):
        """Gets or sets a JSON object describing the service to be created by the publish opertation."""
        return self._props.get("publishParameters")

    @publish_parameters.setter
    def publish_parameters(self, value):
        self._set_nullable("publishParameters", value)

    @property
    def text(self):
        return self._props.get("text")

    @text.setter
    def text(self, value):
        self._set_nullable("text", value)
