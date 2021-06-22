from unittest import TestCase
from app import rm
import tempfile
import os

class TestMyCode(TestCase):

    temp_file = os.path.join(tempfile.gettempdir(), "tmp_test_file")

    def setUp(self) -> None:
        with open(self.temp_file, "wb") as target:
            target.write(b"Delete Me!")
    
    def test_rm(self):
        rm(self.temp_file)
        self.assertFalse(os.path.isfile(self.temp_file), "failed to remove the file.")        
