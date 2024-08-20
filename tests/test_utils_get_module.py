import unittest
from unittest.mock import patch, MagicMock
from fasthtml_extn.utils import get_module


def test_root_module():
    with patch("builtins.__import__") as mock_import:
        mock_module = MagicMock()
        mock_import.return_value = mock_module

        result = get_module("", "test_module")

        mock_import.assert_called_once_with("app.test_module", fromlist=["test_module"])
        assert result == mock_module, f"Expected {mock_module}, got {result}"


def test_nested_module():
    with patch("builtins.__import__") as mock_import:
        mock_module = MagicMock()
        mock_import.return_value = mock_module

        result = get_module("nested/path", "test_module")

        mock_import.assert_called_once_with(
            "app.nested.path.test_module", fromlist=["test_module"]
        )
        assert result == mock_module, f"Expected {mock_module}, got {result}"


if __name__ == "__main__":
    unittest.main()
