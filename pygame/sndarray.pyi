# Portions (c) Microsoft Corporation

from typing import Tuple

import numpy
from . import mixer

def array(sound: mixer.Sound) -> numpy.ndarray: ...
def samples(sound: mixer.Sound) -> numpy.ndarray: ...
def make_sound(array: numpy.ndarray) -> mixer.Sound: ...
def use_arraytype(arraytype: str) -> mixer.Sound: ...
def get_arraytype() -> str: ...
def get_arraytypes() -> Tuple[str]: ...

