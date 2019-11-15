"""pytest root config file"""

import pytest


def pytest_bdd_apply_tag(tag, function):
    """Hook for pytest-bdd tag handling.
    All tests with trace_xyz identifier will be handled with the same
    trace mark. IDs, such as xyz will be handled separately"""
    if tag.startswith("trace_"):
        marker = getattr(pytest.mark, "trace")
        marker(function)
        return True
    # Fall back to pytest-bdd's default behavior
    return None
