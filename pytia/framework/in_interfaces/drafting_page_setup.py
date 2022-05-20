from pytia.framework.in_interfaces.page_setup import PageSetup


class DraftingPageSetup(PageSetup):
    def __init__(self, com_object):
        super().__init__(com_object)
        self.drafting_page_setup = com_object

    @property
    def choose_best_orientation(self) -> bool:
        return self.drafting_page_setup.ChooseBestOrientation

    @choose_best_orientation.setter
    def choose_best_orientation(self, value: bool):
        self.drafting_page_setup.ChooseBestOrientation = value

    @property
    def fit_to_printer_format(self) -> bool:
        return self.drafting_page_setup.FitToPrinterFormat

    @fit_to_printer_format.setter
    def fit_to_printer_format(self, value: bool):
        self.drafting_page_setup.FitToPrinterFormat = value

    @property
    def fit_to_sheet_format(self) -> bool:
        return self.drafting_page_setup.FitToSheetFormat

    @fit_to_sheet_format.setter
    def fit_to_sheet_format(self, value: bool):
        self.drafting_page_setup.FitToSheetFormat = value

    def __repr__(self):
        return f'DraftingPageSetup(name="{ self.name }")'
