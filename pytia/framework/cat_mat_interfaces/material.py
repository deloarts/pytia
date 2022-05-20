from pytia.framework.cat_mat_interfaces.analysis_material import AnalysisMaterial
from pytia.framework.cat_rma_interfaces.rendering_material import RenderingMaterial
from pytia.framework.system_interfaces.any_object import AnyObject


class Material(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.material = com_object

    @property
    def analysis_material(self) -> AnalysisMaterial:
        return AnalysisMaterial(self.material.AnalysisMaterial)

    @property
    def rendering_material(self) -> RenderingMaterial:
        return RenderingMaterial(self.material.RenderingMaterial)

    def copy_rendering_data_from(self, i_rendering_material: RenderingMaterial) -> None:
        return self.material.CopyRenderingDataFrom(i_rendering_material.com_object)

    def create_analysis_data(self, i_label: str) -> AnalysisMaterial:
        return AnalysisMaterial(self.material.CreateAnalysisData(i_label))

    def create_rendering_data(self) -> RenderingMaterial:
        return RenderingMaterial(self.material.CreateRenderingData())

    def exist_analysis_data(self) -> int:
        return self.material.ExistAnalysisData()

    def exist_rendering_data(self) -> int:
        return self.material.ExistRenderingData()

    def get_icon(self, i_path: str) -> None:
        return self.material.GetIcon(i_path)

    def put_icon(self, i_path: str) -> None:
        return self.material.PutIcon(i_path)

    def __repr__(self):
        return f'Material(name="{ self.name }")'
