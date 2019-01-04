import pytest
import util

bot_data = util.start(['oi', 'o que é salic?'])

def test_cumprimentar():
    assert bot_data[1]['intent'] == 'cumprimentar'

def test_salic():
    assert bot_data[5]['intent'] == 'definicao_salic'
