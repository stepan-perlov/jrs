# -*- coding: utf-8 -*-


class JrsError(Exception):
    pass


class JrsSchemaError(JrsError):
    pass


class JrsExportError(JrsError):
    pass
