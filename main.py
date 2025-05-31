from tkinter import Tk

from model.product_filter_model import ProductFilterModel
from view.product_filter_view import ProductFilterView
from controller.product_filter_controller import ProductFilterController

if __name__ == "__main__":
    root = Tk()

    model = ProductFilterModel()
    view = ProductFilterView(root)
    controller = ProductFilterController(model, view)

    root.mainloop()
