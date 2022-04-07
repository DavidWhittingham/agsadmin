from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import (ascii, bytes, chr, dict, filter, hex, input, int, map, next, oct, open, pow, range, round, str,
                      super, zip)

# local imports
from ..._ParamsBase import ParamsBase
from .JobType import JobType


class UserItemStatusParams(ParamsBase):
    """Holds parameter values for the "updateResources" operation on a user content item."""
    @property
    def job_type(self):
        self._get_nullable_enum("jobType", JobType)

    @job_type.setter
    def job_type(self, value):
        self._set_nullable_enum("jobType", value, JobType)

    @property
    def job_id(self):
        self._get_nullable("jobId")

    @job_id.setter
    def job_id(self, value):
        self._set_nullable("jobId", value)
