from .labeling_panel import LabelingPanel, LabelClassesUIList, ObjectLabelsUIList, LabelRulesUIList, NamedEntitiesUIList
from .landmark_section import *


classes = (
    # Labeling panel (classes)
    LabelingPanel, LabelClassesUIList, ObjectLabelsUIList, LabelRulesUIList, NamedEntitiesUIList,

    # Landmarks (rigs, faces)
    RigItem, KeypointItem, SkeletonConnectionItem, PoseLabelSettings, KeypointList,
    ConnectionList, RegisteredSkeletonsList
)