"""
Raven utility functions

"""


def import_module(dotted_path):
    """
    Imports the specified module based on the
    dot notated import path for the module.
    """
    import importlib

    module_parts = dotted_path.split('.')
    module_path = '.'.join(module_parts[:-1])
    module = importlib.import_module(module_path)

    return getattr(module, module_parts[-1])


def initialize_class(data, **kwargs):
    """
    :param data: A string or dictionary containing a import_path attribute.
    """
    if isinstance(data, dict):
        import_path = data.pop('import_path')
        data.update(kwargs)
        Class = import_module(import_path)

        return Class(**data)
    else:
        Class = import_module(data)

        return Class(**kwargs)
