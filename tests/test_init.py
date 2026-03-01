"""Verify package is importable."""

import blender_tools


def test_package_import() -> None:
    assert blender_tools is not None
