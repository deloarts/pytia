from pytia.framework.system_interfaces.any_object import AnyObject


class ProjectedToleranceZone(AnyObject):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.projected_tolerance_zone = com_object

    @property
    def length(self) -> float:
        return self.projected_tolerance_zone.Length

    @property
    def position(self) -> float:
        return self.projected_tolerance_zone.Position

    def get_projected_tol_zone_reference(self, op_reference: tuple) -> tuple:
        return self.projected_tolerance_zone.GetProjectedTolZoneReference(op_reference)

    def __repr__(self):
        return f'ProjectedToleranceZone(name="{ self.name }")'
