from operator import truediv
from turtle import st
import pytest

from domainmodel.artist import Artist


class TestArtist:

    def test_construction(self):
        artist1 = Artist(1, 'Tailor Swift')
        assert str(artist1) == "<Artist Tailor Swift, artist id = 1>"
        artist2 = Artist(2, "Maroon 5")
        assert str(artist2) == '<Artist Maroon 5, artist id = 2>'
        artist3 = Artist(3, 'Kate Bush')
        assert str(artist3) == '<Artist Kate Bush, artist id = 3>'
        artist4 = Artist(4, "bruh    ")
        assert str(artist4) == '<Artist bruh, artist id = 4>'
        artist5 = Artist(5, 45)
        assert str(artist5) == '<Artist None, artist id = 5>'
    
    def test_setter(self):
        artist1 = Artist(1, 'Tailor Swift')
        artist1.full_name = "Rukun"
        assert str(artist1)  == '<Artist Rukun, artist id = 1>'
        artist1.full_name = 3
        assert str(artist1) == '<Artist None, artist id = 1>'
    
    def test_eq(self):
        artist1 = Artist(1, 'Tailor Swift')
        artist2 = Artist(2, "Maroon 5")
        assert (artist1 == artist2) == False
    
    def test_hash(self):
        artist1 = Artist(1, 'Tailor Swift')
        artist2 = Artist(2, "Maroon 5")
        assert (hash(artist1) == hash(artist2)) == False
        assert (hash(artist2) == hash(artist2)) == True
    
    def test_sorting(self):
        artist1 = Artist(1, 'Tailor Swift')
        artist2 = Artist(2, "Maroon 5")
        list1 = [artist2, artist1]
        list1.sort()
        assert str(list1) == '[<Artist Tailor Swift, artist id = 1>, <Artist Maroon 5, artist id = 2>]'

    def test_sets(self):
        artist1 = Artist(1, 'Tailor Swift')
        artist2 = Artist(2, "Maroon 5")
        x = {artist1}
        assert str(x) == '{<Artist Tailor Swift, artist id = 1>}'
        x.add(artist2)
        assert str(x) == '{<Artist Tailor Swift, artist id = 1>, <Artist Maroon 5, artist id = 2>}'
        x.remove(artist2)
        assert str(x) == '{<Artist Tailor Swift, artist id = 1>}'
        x.add(artist1)
        assert str(x) == '{<Artist Tailor Swift, artist id = 1>}'
