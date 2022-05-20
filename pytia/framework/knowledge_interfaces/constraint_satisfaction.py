from pytia.framework.knowledge_interfaces.set_of_equation import SetOfEquation


class ConstraintSatisfaction(SetOfEquation):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.constraint_satisfaction = com_object

    def solve(self) -> None:
        return self.constraint_satisfaction.Solve()

    def __repr__(self):
        return f'ConstraintSatisfaction(name="{ self.name }")'
