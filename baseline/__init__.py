import os

# Several module level utility functions

gpu_project_base_path = '/storage/dldi/PyProjects/SegRelaDet4VidVRDT2'
local_project_base_path = '/home/daivd/PycharmProjects/SegRelaDet4VidVRDT2'

env = 'gpu'

if env == 'gpu':
    project_base_path = gpu_project_base_path
else:
    project_base_path = local_project_base_path

vidvrd_baseline_output_path = os.path.join(project_base_path, 'baseline/output')


def get_segment_signature(vid, fstart, fend):
    """
    Generating video clip signature string
    """
    return '{}-{:04d}-{:04d}'.format(vid, fstart, fend)


def get_feature_path(name, vid):
    """
    Path to save intermediate object trajectory proposals and features
    """
    feature_path = os.path.join(vidvrd_baseline_output_path, 'features', name)
    if not os.path.exists(feature_path):
        os.makedirs(feature_path)
    feature_path = os.path.join(feature_path, vid)
    if not os.path.exists(feature_path):
        os.makedirs(feature_path)
    return feature_path


def get_model_path():
    """
    Path to save trained model
    """
    model_path = os.path.join(vidvrd_baseline_output_path, 'models')
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    return model_path


def segment_video(fstart, fend):
    """
    Given the duration [fstart, fend] of a video, segment the duration
    into many 30-frame segments with overlapping of 15 frames
    """
    segs = [(i, i + 30) for i in range(fstart, fend - 30 + 1, 15)]
    return segs
