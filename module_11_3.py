import inspect
from pprint import pprint


class Object:
    pass


def introspection_info(obj_):
    type_ = type(obj_).__name__
    attribute = getattr(obj_, '__dict__', None)
    methods = dir(obj_)
    module = obj_.__class__.__module__
    func = inspect.isfunction(obj_)
    info = {'type': type_, 'attributes': attribute, 'methods': methods, 'module': module, 'function': func}
    return info


obj = Object()
number_info = introspection_info(42)
pprint(number_info)
