from enum import Enum


class LayerType(Enum):
    """
    The defined Heatmap Layer types
    """
    HEALTH = 'HEALTH_LAYER'
    CRIME = 'CRIME_LAYER'
    COMPLAINT = 'COMPLAINT_LAYER'
