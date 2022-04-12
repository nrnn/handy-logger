# -*- coding: utf-8 -*-

import sys
import yaml


def currentframe():
    """Return the frame object for the caller's stack frame."""
    f = sys._getframe(1) if hasattr(sys, "_getframe") else None
    if f:
        return f.f_back
    try:
        raise Exception
    except Exception:
        e = sys.exc_info()
        return e[2].tb_frame.f_back


def get_caller_module_name(stacklevel=1):
    """
    Get the module and function name of stack frame.
    :param stacklevel: Default is 1, means return the name of module and function from which this method is invoked.
    :return:
    """
    f = currentframe()
    while stacklevel > 0:
        f = f.f_back
        stacklevel -= 1
    return f.f_globals["__name__"], f.f_code.co_name


def load_yaml_to_dict(yaml_path, encoding="utf-8"):
    with open(yaml_path, 'r', encoding=encoding) as f:
        return yaml.safe_load(f.read())
