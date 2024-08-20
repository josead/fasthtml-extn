import unittest
import os
from fasthtml_extn.utils import (
    get_path_and_route,
)

# Set up a common app_dir for all tests
APP_DIR = "/home/user/workspace/web_application"


def test_same_directory():
    directory = APP_DIR
    relative_path, route = get_path_and_route(directory, APP_DIR)
    assert relative_path == "", f"Expected empty string, got {relative_path}"
    assert route == "/", f"Expected '/', got {route}"


def test_subdirectory():
    directory = os.path.join(APP_DIR, "subdir")
    relative_path, route = get_path_and_route(directory, APP_DIR)
    assert relative_path == "subdir", f"Expected 'subdir', got {relative_path}"
    assert route == "/subdir", f"Expected '/subdir', got {route}"


def test_nested_subdirectory():
    directory = os.path.join(APP_DIR, "subdir", "nested")
    relative_path, route = get_path_and_route(directory, APP_DIR)
    assert relative_path == os.path.join(
        "subdir", "nested"
    ), f"Expected 'subdir/nested', got {relative_path}"
    assert route == "/subdir/nested", f"Expected '/subdir/nested', got {route}"


def test_app_directory():
    directory = os.path.join(APP_DIR, "app")
    relative_path, route = get_path_and_route(directory, APP_DIR)
    assert relative_path == "app", f"Expected 'app', got {relative_path}"
    assert route == "/", f"Expected '/', got {route}"


def test_parent_directory():
    directory = os.path.dirname(APP_DIR)
    relative_path, route = get_path_and_route(directory, APP_DIR)
    assert relative_path == "..", f"Expected '..', got {relative_path}"
    assert route == "/..", f"Expected '/..', got {route}"


if __name__ == "__main__":
    unittest.main()
