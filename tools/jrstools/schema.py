# -*- coding: utf-8 -*-
import io
from copy import deepcopy
import subprocess

import yaml

from error import JrsSchemaError


def load_schemas(root):
    schemas = {}
    res = subprocess.check_output(["find", root, "-name", "*.yaml"])
    for fpath in res.split():
        with io.open(fpath, encoding="utf-8") as fstream:
            s = yaml.load(fstream)
            if "id" not in s:
                raise JrsSchemaError("In root schema id must exists. file: {}".format(fpath))
            schemas[s["id"]] = s
    return schemas


def _replace_ref(value, node_key, parent, root, store):
    if not type(value) in [str, unicode]:
        raise JrsSchemaError("Invalid $ref value type(allowed str, unicode) - {}. node - {}.{}".format(value, parent, node_key))

    try:
        index = value.index("#")
        if index != value.rindex("#"):
            raise JrsSchemaError("Invalid $ref value(exists more than one '#') - {}. node - {}.{}".format(value, parent, node_key))

        if index == 0:
            path = value.strip("#")
            obj = root
        else:
            split = value.split("#")
            obj = store[split[1]]
            path = split[2]

        if path == "":
            parent[node_key] = deepcopy(obj)
        elif path.startswith("/"):
            for key in path.lstrip("/").split("/"):
                obj = obj[key]
            parent[node_key] = deepcopy(obj)
        else:
            raise JrsSchemaError("Invalid $ref value(after '#' must be '/') - {}. node - {}.{}".format(value, parent, node_key))

        parent[node_key]["resolved_$ref"] = value

    except ValueError:
        raise JrsSchemaError("Invalid $ref value('#' not exists) - {}. node - {}.{}".format(value, parent, node_key))


def _resolve_refs(node, node_key, parent, root, store):
    if type(node) == dict:
        for key, value in node.iteritems():
            if key == "$ref":
                _replace_ref(value, node_key, parent, root, store)
            elif type(value) in [dict, list]:
                _resolve_refs(value, key, node, root, store)
    elif type(node) == list:
        for i, value in enumerate(node):
            if type(value) in [dict, list]:
                _resolve_refs(value, i, node, root, store)


def resolve_schemas(schemas):
    for sch in schemas.itervalues():
        if "$ref" in unicode(sch):
            _resolve_refs(sch, None, None, sch, schemas)
        for schKey, schValue in sch.iteritems():
            if type(schValue) == dict:
                schValue["$schema"] = "http://json-schema.org/draft-04/schema#"

    return schemas


def _clear_recursive(node):
    if type(node) == dict:
        if "title" in node:
            del node["title"]
        if "description" in node:
            del node["description"]
        if "resolved_$ref" in node:
            del node["resolved_$ref"]

        for value in node.itervalues():
            _clear_recursive(value)
    elif type(node) == list:
        for value in node:
            _clear_recursive(value)


def clear_schemas(schemas):
    schemasCopy = deepcopy(schemas)
    _clear_recursive(schemasCopy)
    return schemasCopy


def split_schemas(schemas):
    pass
