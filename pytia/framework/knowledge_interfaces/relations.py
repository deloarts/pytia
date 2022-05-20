from typing import Iterator
from pathlib import Path
from pytia.framework.exception_handling.exceptions import CATIAApplicationException
from pytia.framework.knowledge_interfaces.check import Check
from pytia.framework.knowledge_interfaces.design_table import DesignTable
from pytia.framework.knowledge_interfaces.formula import Formula
from pytia.framework.knowledge_interfaces.law import Law
from pytia.framework.knowledge_interfaces.optimizations import Optimizations
from pytia.framework.knowledge_interfaces.relation import Relation
from pytia.framework.knowledge_interfaces.rule import Rule
from pytia.framework.knowledge_interfaces.set_of_equation import SetOfEquation
from pytia.framework.system_interfaces.any_object import AnyObject
from pytia.framework.system_interfaces.collection import Collection
from pytia.framework.cat_types.general import cat_variant


class Relations(Collection):
    def __init__(self, com_object):
        super().__init__(com_object, child_object=Relation)
        self.relations = com_object

    @property
    def optimizations(self) -> Optimizations:
        return Optimizations(self.relations.Optimizations)

    def create_check(self, i_name: str, i_comment: str, i_check_body: str) -> Check:
        return Check(self.relations.CreateCheck(i_name, i_comment, i_check_body))

    def create_design_table(
        self, i_name: str, i_comment: str, i_copy_mode: bool, i_sheet_path: Path
    ) -> DesignTable:
        if not i_sheet_path.exists():
            raise CATIAApplicationException(
                f'Could not find design table "{i_sheet_path}".'
            )
        return DesignTable(
            self.relations.CreateDesignTable(
                i_name, i_comment, i_copy_mode, i_sheet_path
            )
        )

    def create_formula(self, i_name, i_comment, i_output_parameter, i_formula_body):
        return Formula(
            self.relations.CreateFormula(
                i_name, i_comment, i_output_parameter.com_object, i_formula_body
            )
        )

    def create_horizontal_design_table(
        self, i_name: str, i_comment: str, i_copy_mode: bool, i_sheet_path: str
    ) -> DesignTable:
        return DesignTable(
            self.relations.CreateHorizontalDesignTable(
                i_name, i_comment, i_copy_mode, i_sheet_path
            )
        )

    def create_law(self, i_name: str, i_comment: str, i_law_body: str) -> Law:
        return Law(self.relations.CreateLaw(i_name, i_comment, i_law_body))

    def create_program(self, i_name: str, i_comment: str, i_program_body: str) -> Rule:
        return Rule(self.relations.CreateProgram(i_name, i_comment, i_program_body))

    def create_rule_base(self, i_name: str) -> Relation:
        return Relation(self.relations.CreateRuleBase(i_name))

    def create_set_of_equations(
        self, i_name: str, i_comment: str, i_formula_body: str
    ) -> SetOfEquation:
        return SetOfEquation(
            self.relations.CreateSetOfEquations(i_name, i_comment, i_formula_body)
        )

    def create_set_of_relations(self, i_parent: AnyObject) -> None:
        return self.relations.CreateSetOfRelations(i_parent.com_object)

    def generate_xml_report_for_checks(self, i_name: str) -> None:
        return self.relations.GenerateXMLReportForChecks(i_name)

    def item(self, i_index: cat_variant) -> Relation:
        return Relation(self.relations.Item(i_index))

    def remove(self, i_index: cat_variant) -> None:
        return self.relations.Remove(i_index)

    def sub_list(self, i_feature: AnyObject, i_recursively: bool) -> "Relations":
        return Relations(self.relations.SubList(i_feature.com_object, i_recursively))

    def __getitem__(self, n: int) -> Relation:
        if (n + 1) > self.count:
            raise StopIteration
        return Relation(self.relations.item(n + 1))

    def __iter__(self) -> Iterator[Relation]:
        for i in range(self.count):
            yield self.child_object(self.com_object.item(i + 1))

    def __repr__(self):
        return f'Relations(name="{self.name}")'
