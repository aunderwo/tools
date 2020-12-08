#!/usr/bin/env python

import os
import yaml
import nf_core.lint

def test_files_exist_missing_config(self):
    """Lint test: critical files missing FAIL"""
    new_pipeline = self._make_pipeline_copy()

    os.remove(os.path.join(new_pipeline, "nextflow.config"))

    lint_obj = nf_core.lint.PipelineLint(new_pipeline)
    lint_obj._load()

    results = lint_obj.files_exist()
    assert results["failed"] == ["File not found: `nextflow.config`"]

def test_files_exist_missing_main(self):
    """Check if missing main issues warning"""
    new_pipeline = self._make_pipeline_copy()

    os.remove(os.path.join(new_pipeline, "main.nf"))

    lint_obj = nf_core.lint.PipelineLint(new_pipeline)
    lint_obj._load()

    results = lint_obj.files_exist()
    assert results["warned"] == ["File not found: `main.nf`"] 

def test_files_exist_depreciated_file(self):
    """Check whether depreciated file issues warning"""
    new_pipeline = self._make_pipeline_copy()

    nf = os.path.join(new_pipeline, "parameters.settings.json")
    os.system("touch {}".format(nf))

    lint_obj = nf_core.lint.PipelineLint(new_pipeline)
    lint_obj._load()

    results = lint_obj.files_exist()
    assert results["failed"] == ["File must be removed: `parameters.settings.json`"]
    
