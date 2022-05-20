from pytia.framework.in_interfaces.reference import Reference
from pytia.framework.in_interfaces.workbench import Workbench
from pytia.framework.space_analyses_interfaces.clashes import Clashes
from pytia.framework.space_analyses_interfaces.distances import Distances
from pytia.framework.space_analyses_interfaces.inertias import Inertias
from pytia.framework.space_analyses_interfaces.measurable import Measurable
from pytia.framework.space_analyses_interfaces.sections import Sections


class SPAWorkbench(Workbench):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.spa_workbench = com_object.GetWorkbench("SPAWorkbench")

    @property
    def clashes(self) -> Clashes:
        return Clashes(self.spa_workbench.Clashes)

    @property
    def distances(self) -> Distances:
        return Distances(self.spa_workbench.Distances)

    @property
    def inertias(self) -> Inertias:
        return Inertias(self.spa_workbench.Inertias)

    @property
    def sections(self) -> Sections:
        return Sections(self.spa_workbench.Sections)

    def get_measurable(self, i_measured_item: Reference) -> Measurable:
        return Measurable(self.spa_workbench.GetMeasurable(i_measured_item.com_object))

    def __repr__(self):
        return f'SpaWorkbench(name="{self.name}")'
