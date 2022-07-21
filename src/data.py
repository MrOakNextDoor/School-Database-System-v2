
#   Libraries
import json
import os
from abc import ABC, abstractmethod
from typing import Any, Dict

import constants


#   Code
class Data(ABC):
    def __init__(self) -> None:
        pass

    def from_dict(self, data: Dict[str, Any]) -> None:
        """Load the object's data from a dictionary.

        Args:
            data (Dict[str, Any]): Dictionary to be used.
        """

        for key, value in filter(lambda x: not x[0].startswith('_'), 
            data.values()):
            try:
                self.__dict__[key] = value
            except KeyError:
                continue

    def to_dict(self) -> Dict[str, Any]:
        return filter(lambda x: not x[0].startswith('_'), self.__dict__)

class DataLoader(Data):
    def __init__(self, path: str) -> None:
        super().__init__()
        
        self.path = path

        self.load()

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        if value != self.path:
            try:
                os.remove(self.path)
            except OSError:
                pass
            finally:
                self._path = value
                self.dump()

    @abstractmethod
    def load(self) -> None:
        pass

    @abstractmethod
    def loads(self, s: str) -> None:
        pass

    @abstractmethod
    def dump(self) -> None:
        pass

    @abstractmethod
    def dumps(self) -> str:
        pass

class JsonDataLoader(DataLoader):
    def __init__(self, path: str) -> None:
        
        super().__init__(path)

    def load(self) -> None:
        """Load information from a json file specified in __init__.
        """

        with open(self.path, 'r', encoding='utf-8') as f:
            self.from_dict(json.load(f))

    def loads(self, s: str) -> None:
        """Load information from a json-formatted string.

        Args:
            s (str): Json-formatted string.
        """

        self.from_dict(json.loads(s))

    def dump(self) -> None:
        """Dump the information to a json file specified in __init__.
        """

        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4, 
                sort_keys=True)

    def dumps(self) -> str:
        """Return a json-formatted string containing the DataLoader's 
        information

        Returns:
            str: Json-formatted string.
        """

        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4, 
            sort_keys=True)

class Settings(JsonDataLoader):
    def __init__(self, path: str) -> None:
        super().__init__(self)
