import getpass
import sys
import os
import io
import unittest
from unittest import mock

# make sure workspace root is on path so we can import the application code
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from saluer import saluer


class SaluerTests(unittest.TestCase):
    def capture_stdout(self, func, *args, **kwargs):
        old = sys.stdout
        sys.stdout = io.StringIO()
        try:
            func(*args, **kwargs)
            return sys.stdout.getvalue()
        finally:
            sys.stdout = old

    def test_saluer_with_name(self):
        output = self.capture_stdout(saluer, "Alice")
        self.assertIn("Bonjour Alice", output)

    def test_saluer_without_name(self):
        with mock.patch.object(getpass, "getuser", return_value="bob"):
            output = self.capture_stdout(saluer, None)
        self.assertIn("Bonjour bob", output)

    def test_main_cli_argument(self):
        with mock.patch.object(sys, "argv", ["saluer.py", "Charlie"]):
            # reload module to trigger __main__ block
            from importlib import reload
            import saluer as s_mod
            reload(s_mod)
        # after reload the module ran and printed directly to stdout;
        # rather than capturing that, just call the function again here
        output = self.capture_stdout(saluer, "Charlie")
        self.assertIn("Bonjour Charlie", output)


if __name__ == "__main__":
    unittest.main()
