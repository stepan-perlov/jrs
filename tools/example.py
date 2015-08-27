#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from jrstools import load_schemas, resolve_schemas
from jrstools import export_json, export_js

SCHEMAS_DIR = os.path.join(os.path.dirname(__file__), "schemas_example")
BUILD_DIR = os.path.join(os.path.dirname(__file__), "../build")

schemas = resolve_schemas(load_schemas(SCHEMAS_DIR))

if not os.path.exists(BUILD_DIR):
    os.mkdir(BUILD_DIR)

export_json(BUILD_DIR, schemas)
export_js("{}/build.js".format(BUILD_DIR), schemas)
