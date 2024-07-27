from PyNite import PhysMember, Member3D

import plotly.graph_objects as go

def frame_element_traces(
    frame_element: PhysMember
) -> list[go.Trace]:
    """
    Returns a plotly Scatter3D trace from a PyNite.Member object
    """
    phys_member_name = frame_element.name
    elements = frame_element.sub_members # dict

    all_traces = []
    for element_name, member3d in elements.items():
        member_traces = create_element_traces(phys_member_name, element_name, member3d)
        point_load_traces = create_element_point_load_traces(element_name, member3d)
        dist_load_traces = create_element_dist_load_traces(element_name, member3d)
        all_traces += member_traces + point_load_traces + dist_load_traces
    return all_traces


def create_element_traces(phys_member_name: str, element_name: str, member: Member3D) -> list[go.Trace]:
    """
    Returns an element trace
    """
    pass

    

