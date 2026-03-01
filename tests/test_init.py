"""Verify package is importable."""

import blender_tools


def test_package_import() -> None:
    assert blender_tools is not None


def test_version() -> None:
    assert blender_tools.__version__ == "0.1.0"
