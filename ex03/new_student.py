import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates an id made of 15 random letters.

    Args:
        None

    Returns:
        - The generated id as a string.

    Raises:
        None
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass(init=True)
class Student:
    """
    Dataclass that contains information about students.

    Attributes:
        - name(str): First name of the student.
        - surname(str): Family name of the student.
        - active(bool), optional: Boolean that describes the activity status.
        - login(str), no init: Login name that is created from the first letter
        of the first name and up to the first seven letters of the family name.
        Cannot be provided for initialization.
        - id(str), no init: randomly generated ascii string used for
        identification, cannot be provided for initialization.

    Methods:
        __post_init__: method that is called right after initialization.
        Sets the value of self.login.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """
        Called right after initialization. Sets the value of self.login.
        """
        self.login = self.name[:1].lower()+self.surname[:7].lower()
