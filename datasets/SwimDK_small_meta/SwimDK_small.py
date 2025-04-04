
#https://mmpose.readthedocs.io/en/latest/advanced_guides/customize_datasets.html

dataset_info = dict(
    dataset_name='coco',
    paper_info=dict(
        author='Thomas Charton-Jaeg and Pedro Prazeres',
        title='SwimDK_small',
        container='Dive analysis BSc Project',
        year='2025',
        homepage='',
    ),
    keypoint_info = {
    0: dict(name='right_wrist', id=0, color=[225, 38, 9], type='upper', swap='left_wrist'),
    1: dict(name='right_elbow', id=1, color=[225, 38, 9], type='upper', swap='left_elbow'),
    2: dict(name='right_shoulder', id=2, color=[225, 38, 9], type='upper', swap='left_shoulder'),
    3: dict(name='right_hip', id=3, color=[225, 38, 9], type='lower', swap='left_hip'),
    4: dict(name='right_knee', id=4, color=[225, 38, 9], type='lower', swap='left_knee'),
    5: dict(name='right_ankle', id=5, color=[255, 26, 56], type='lower', swap='left_ankle'),
    6: dict(name='left_wrist', id=6, color=[0, 189, 31], type='upper', swap='right_wrist'),
    7: dict(name='left_elbow', id=7, color=[0, 189, 31], type='upper', swap='right_elbow'),
    8: dict(name='left_shoulder', id=8, color=[0, 189, 31], type='upper', swap='right_shoulder'),
    9: dict(name='left_hip', id=9, color=[0, 189, 31], type='lower', swap='right_hip'),
    10: dict(name='left_knee', id=10, color=[0, 189, 31], type='lower', swap='right_knee'),
    11: dict(name='left_ankle', id=11, color=[0, 189, 31], type='lower', swap='right_ankle'),
    12: dict(name='nose', id=12, color=[28, 49, 212], type='upper', swap=''),
    13: dict(name='right_eye', id=13, color=[196, 89, 217], type='upper', swap='left_eye'),
    14: dict(name='left_eye', id=14, color=[21, 190, 193], type='upper', swap='right_eye')
},
    skeleton_info = {
    0: dict(link=('right_elbow', 'right_shoulder'), id=0, color=[225, 38, 9]),
    1: dict(link=('right_shoulder', 'right_hip'), id=1, color=[225, 38, 9]),
    2: dict(link=('right_hip', 'right_knee'), id=2, color=[225, 38, 9]),
    3: dict(link=('right_hip', 'nose'), id=3, color=[225, 38, 9]),
    4: dict(link=('right_hip', 'left_hip'), id=4, color=[225, 38, 9]),
    5: dict(link=('right_knee', 'right_ankle'), id=5, color=[225, 38, 9]),
    6: dict(link=('left_elbow', 'left_shoulder'), id=6, color=[0, 189, 31]),
    7: dict(link=('left_shoulder', 'left_hip'), id=7, color=[0, 189, 31]),
    8: dict(link=('left_hip', 'left_knee'), id=8, color=[0, 189, 31]),
    9: dict(link=('left_knee', 'left_ankle'), id=9, color=[0, 189, 31]),
    10: dict(link=('nose', 'right_eye'), id=10, color=[28, 49, 212]),
    11: dict(link=('nose', 'left_eye'), id=11, color=[28, 49, 212]),
    12: dict(link=('right_eye', 'left_eye'), id=12, color=[196, 89, 217]),
    13: dict(link=('right_elbow', 'right_wrist'), id=13, color=[225, 38, 9]),
    14: dict(link=('left_elbow', 'left_wrist'), id=14, color=[0, 189, 31])
},
    # TODO: mess with this
    joint_weights = [
    1.5,  # right_wrist
    1.2,  # right_elbow
    1.0,  # right_shoulder
    1.0,  # right_hip
    1.0,  # right_knee
    1.0,  # right_ankle
    1.5,  # left_wrist
    1.2,  # left_elbow
    1.0,  # left_shoulder
    1.0,  # left_hip
    1.0,  # left_knee
    1.0,  # left_ankle
    1.0,  # nose
    1.2,  # right_eye
    1.2   # left_eye
],
    # TODO: mess with this
    sigmas = [
    0.062,  # right_wrist
    0.072,  # right_elbow
    0.025,  # right_shoulder
    0.035,  # right_hip
    0.035,  # right_knee
    0.079,  # right_ankle
    0.062,  # left_wrist
    0.072,  # left_elbow
    0.025,  # left_shoulder
    0.035,  # left_hip
    0.035,  # left_knee
    0.079,  # left_ankle
    0.026,  # nose
    0.087,  # right_eye
    0.087   # left_eye
])