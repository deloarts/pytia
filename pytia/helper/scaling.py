"""
    Helper module for scaling.
"""

from pycatia.drafting_interfaces.drawing_view import DrawingView

from pytia.log import log


def get_view_scale(view: DrawingView, max_width: float, max_height: float) -> float:
    """
    Returns the scale for a view to fit into the given maximum dimensions.

    Args:
        view (DrawingView): The drawing view to scale.
        max_width (float): The maximum width.
        max_height (float): The maximum height.

    Returns:
        float: The scale for the drawing view.
    """
    x_min, x_max, y_min, y_max = view.size()
    width = x_max - x_min
    height = y_max - y_min

    scale = (
        max_width / width
        if (width_ratio := width / max_width) > (height_ratio := height / max_height)
        else max_height / height
    )
    log.debug(
        f"Width ratio is {round(width_ratio, 2)} ({round(width, 2)}/{round(max_width, 2)}). "
        f"Height ratio is {round(height_ratio, 2)} ({round(height, 2)}/{round(max_height, 2)})"
    )
    log.info(f"Set scale for view {view.name!r} to {round(view.scale, 2)}")
    return scale
