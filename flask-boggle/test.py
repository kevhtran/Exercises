from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        """Stuff to do before every test."""
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure info is in teh session and HTML is displayed"""
        with app.test_client() as client:
            response = client.get('/')
            self.assertIn('game_board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)

    def test_valid_word(self):
        """Test if word is valid by modifying the board in the session"""

        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['game_board'] = [["C", "A", "T", "T", "T"],
                                      ["C", "A", "T", "T", "T"],
                                      ["C", "A", "T", "T", "T"],
                                      ["C", "A", "T", "T", "T"],
                                      ["C", "A", "T", "T", "T"]]
        response = client.get('/check-word?word=cat')
        self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        """Test if word is in the dictionary"""
        with app.test_client() as client:
            client.get('/')
            response = client.get('/check-word?word=impossible')
            self.assertEqual(response.json['result'], 'not-on-board')

    def non_english_word(self):
        """Test if word is on the board"""
        with app.test_client() as client:
            client.get('/')
            response = client.get('/check-word?word=fsjdakfkldsfjdslkfjdlksf')
            self.assertEqual(response.json['result'], 'not-word')
