from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from myTracker.models.head.myTracker import UPChannelMyTracker, DepthwiseMyTracker, MultiMyTracker


myTrackers = {
        'UPChannelMyTracker': UPChannelMyTracker,
        'DepthwiseMyTracker': DepthwiseMyTracker,
        'MultiMyTracker': MultiMyTracker
       }


def get_trackers_head(name, **kwargs):
    return myTrackers[name](**kwargs)

