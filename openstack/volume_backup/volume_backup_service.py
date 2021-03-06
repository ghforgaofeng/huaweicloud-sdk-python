# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack import service_filter


class VolumeBackupService(service_filter.ServiceFilter):
    """The Volume Backup service."""

    valid_versions = [service_filter.ValidVersion('v1'),
                      service_filter.ValidVersion('v2')]

    def __init__(self, version=None):
        """Create Volume Backup service."""
        super(VolumeBackupService, self).__init__(service_type='volume-backup',
                                                  version=version)
