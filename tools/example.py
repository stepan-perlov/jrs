#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from jrstools import load_schemas, resolve_schemas, clear_schemas
from jrstools import export_json, export_js
from jrstools import make_docs

MODULE_DIR = os.path.abspath(os.path.dirname(__file__))
SCHEMAS_DIR = os.path.join(MODULE_DIR, "schemas_example")
BUILD_DIR = os.path.join(MODULE_DIR, "../build")

schemas = resolve_schemas(load_schemas(SCHEMAS_DIR))
clearedSchemas = clear_schemas(schemas)

if not os.path.exists(BUILD_DIR):
    os.mkdir(BUILD_DIR)

export_js(os.path.join(BUILD_DIR, "build.js"), clearedSchemas)
export_json(BUILD_DIR, clearedSchemas)

DOCS_DIR = os.path.join(BUILD_DIR, "docs")
if not os.path.exists(DOCS_DIR):
    os.mkdir(DOCS_DIR)

make_docs(DOCS_DIR, schemas)
