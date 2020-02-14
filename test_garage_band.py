import pytest
from garage_band import Band, Musician, Guitarist, Bassist, Drummer, Singer


def rock():
    radiohead = Band('radiohead')
    assert "Lets do this" == radiohead.moment_of_fame()


def test_class():
    charlie = Guitarist
    assert charlie.instrument == 'guitar'


