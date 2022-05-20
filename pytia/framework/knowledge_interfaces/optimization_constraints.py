from typing import Iterator
from pytia.framework.knowledge_interfaces.optimization_constraint import (
    OptimizationConstraint,
)
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class OptimizationConstraints(Collection):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.optimization_constraints = com_object

    def add_constraint(self, constraint_expression: str) -> OptimizationConstraint:
        return OptimizationConstraint(
            self.optimization_constraints.AddConstraint(constraint_expression)
        )

    def item(self, i_index: cat_variant) -> OptimizationConstraint:
        return OptimizationConstraint(self.optimization_constraints.Item(i_index))

    def remove_constraint(self, i_index: cat_variant) -> None:
        return self.optimization_constraints.RemoveConstraint(i_index)

    def __getitem__(self, n: int) -> OptimizationConstraint:
        if (n + 1) > self.count:
            raise StopIteration
        return OptimizationConstraint(self.optimization_constraints.item(n + 1))

    def __iter__(self) -> Iterator[OptimizationConstraint]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'OptimizationConstraints(name="{self.name}")'
