from PyNite import FEModel3D
from PyNite.PhysMember import PhysMember
from PyNite.Member3D import Member3D
from PyNite.Node3D import Node3D

import plotly.graph_objects as go

def trace_frame_elements(
    model: FEModel3D
) -> list[go.Trace]:
    nodes = model.Nodes
    all_frames = []
    for phys_member in model.Members.values():
        frame_traces = frame_element_traces(phys_member, nodes)
        all_frames += frame_traces
    return all_frames


def frame_element_traces(
    frame_element: PhysMember,
    nodes: dict[str, Node3D],
    **kwargs
) -> list[go.Trace]:
    """
    Returns a plotly Scatter3D trace from a PyNite.Member object
    """
    phys_member_name = frame_element.name
    elements = frame_element.sub_members # dict

    all_traces = []
    for element_name, member3d in elements.items():
        member_trace = create_element_trace(phys_member_name, nodes, member3d)
        # point_load_traces = create_element_point_load_traces(element_name, member3d)
        # dist_load_traces = create_element_dist_load_traces(element_name, member3d)
        all_traces.append(member_trace)
    return all_traces


def create_element_trace(phys_member_name: str, nodes: dict[str, Node3D], member: Member3D, **kwargs) -> go.Trace:
    """
    Returns an element trace
    """
    i_node = member.i_node
    j_node = member.j_node
    #material_name = member.material_name
    # section_name = member.section_name
    
    trace = go.Scatter3d(
        x=(i_node.X, j_node.X), 
        y=(i_node.Y, j_node.Y),
        z=(i_node.Z, j_node.Z),
        mode='lines',
        line={'color': '#999999'},
    )
    return trace


def get_fixity_colors(fixity: tuple[int]) -> str:
    """
    Returns an HTML string describing a color to correspond with the fixity condition
    """
    DX, DY, DZ, RX, RY, RZ = fixity
    max_value = 255
    increment = max_value // 3

    fixity_X = (DX * increment, RX * 2 * increment)
    fixity_Y = (DY * increment, RY * 2 * increment)
    fixity_Z = (DZ * increment, RZ * 2 * increment)

    hex_x = hex(max_value - fixity_X[0] - fixity_X[1]).lstrip("0x")
    hex_y = hex(max_value - fixity_Y[0] - fixity_Y[1]).lstrip("0x")
    hex_z = hex(max_value - fixity_Z[0] - fixity_Z[1]).lstrip("0x")

    return f"#{hex_x}{hex_y}{hex_z}"

    

