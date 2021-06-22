from app import rm
from unittest import mock
from unittest import TestCase

class TestMyCode(TestCase):
   
    @mock.patch("app.os")
    def test_rm(self, mock_os):
        rm("any path")        
        mock_os.remove.assert_called_with("any path")