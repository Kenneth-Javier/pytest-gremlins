"""Root pytest configuration for pytest-gremlins.

This conftest.py handles marker application for ALL tests including doctests.
The tests/conftest.py handles test-specific fixtures.
"""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(
    config: pytest.Config,  # noqa: ARG001
    items: list[pytest.Item],
) -> None:
    """Automatically apply size markers based on test location.

    This hook runs before pytest-test-categories checks for markers.
    """
    for item in items:
        # Get the path parts from the item's path
        item_path = Path(str(item.fspath))
        path_parts = item_path.parts

        if 'small' in path_parts:
            item.add_marker(pytest.mark.small)
        elif 'medium' in path_parts:
            item.add_marker(pytest.mark.medium)
        elif 'large' in path_parts:
            item.add_marker(pytest.mark.large)
        elif 'src' in path_parts:
            # Doctests from source code default to small
            item.add_marker(pytest.mark.small)
