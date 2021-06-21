from unittest import TestCase
from unittest.mock import Mock


class TestTelegram(TestCase):
    def test_telegram_send_message(self):
        MockTelegram = Mock()
        MockTelegram.send.return_value = [
            {
                "id" : 1234,
                "text" : "test text"
            }
        ]
        response = MockTelegram.send()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

