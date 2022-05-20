from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.cat_base_dispatch import CATBaseDispatch


class DrawingViewGenerativeLinks(CATBaseDispatch):
    def __init__(self, com_object):
        super().__init__()
        self.drawing_view_generative_links = com_object

    def add_link(self, i_link: AnyObject) -> None:
        return self.drawing_view_generative_links.AddLink(i_link.com_object)

    def copy_links_to(self, i_links: "DrawingViewGenerativeLinks") -> None:
        return self.drawing_view_generative_links.CopyLinksTo(
            i_links.drawing_view_generative_links
        )

    def first_link(self) -> AnyObject:
        return AnyObject(self.drawing_view_generative_links.FirstLink())

    def next_link(self) -> AnyObject:
        return AnyObject(self.drawing_view_generative_links.NextLink())

    def remove_all_links(self) -> None:
        return self.drawing_view_generative_links.RemoveAllLinks()

    def __repr__(self):
        return f"DrawingViewGenerativeLinks()"
