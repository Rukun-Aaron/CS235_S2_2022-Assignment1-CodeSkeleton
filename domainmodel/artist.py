class Artist:
    def __init__(self, artist_id: int, full_name: str):
        # TODO
        if isinstance(artist_id, int) and artist_id >0:
            self.__artist_id = artist_id
        else:
            self.__artist_id = None
            raise ValueError()
            
        
        if isinstance(full_name, str) and len(full_name.strip()) > 0:

            self.__full_name = full_name.strip()
        else:
            self.__full_name = None

    @property
    def artist_id(self) -> int:
        return self.__artist_id

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, new_full_name):
        # TODO
        if isinstance(new_full_name, str) and len(new_full_name.strip()) > 0:

            self.__full_name = new_full_name.strip()
        else:
            self.__full_name = None

    def __repr__(self):
        # we use access via the property here
        return f"<Artist {self.full_name}, artist id = {self.artist_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.artist_id == other.artist_id

    def __lt__(self, other):
        # TODO
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.artist_id < other.artist_id

    def __hash__(self):
        # TODO
        return hash(self.artist_id)

if __name__ =='__main__':
    a = Artist(1 ,"Test")
    b = Artist(1, "Test")
    print(hash(a)== hash(b))

    