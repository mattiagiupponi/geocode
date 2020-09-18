import os
import unittest
from io import StringIO

from django.core import management


class CommandTests(unittest.TestCase):
    def test_import_csv_with_invalid_file_path(self):
        out = StringIO()
        management.call_command("importcsv", "abcd", stdout=out)
        self.assertEquals(
            "File does not exists, please check the file_path: abcd",
            out.getvalue().replace("\n", ""),
        )

    def test_import_csv_with_valid_file_path(self):
        out = StringIO()
        test_file_path = (
            f"{os.path.dirname(os.path.abspath(__file__))}/utils/testcsv.csv"
        )
        management.call_command("importcsv", test_file_path, stdout=out)
        self.assertEquals("File successfully loaded", out.getvalue().replace("\n", ""))


if __name__ == "__main__":
    unittest.main()
