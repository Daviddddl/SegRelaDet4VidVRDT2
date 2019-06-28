import json
import os
from config import track_project_base_path


def get_det_tracking(vid_dir, vid):
    track_file_path = os.path.join(track_project_base_path, 'framesCache', vid_dir, vid, 'tracking.json')
    with open(track_file_path, 'r') as in_f:
        tracking_json = json.load(in_f)
    return tracking_json['obj_tracking']


