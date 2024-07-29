from PyNite import FEModel3D
from plotly.graph_objects import Layout, Figure
from . import frames


def create_figure(model: FEModel3D) -> Figure:
    layout = default_layout()
    frame = frames.trace_frame_elements(model)
    print(frame)
    return Figure(data=frame, layout=layout)


def default_layout():
    return Layout()