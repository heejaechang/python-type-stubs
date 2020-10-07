# Portions (c) Microsoft Corporation

from typing import Optional, Sequence, Tuple, Union

from . import color
from . import math
from . import rect
from . import surface

_Coordinate = Union[Tuple[float, float], Sequence[float], math.Vector2]
_ColorValue = Union[color.Color, Tuple[int, int, int], Sequence[int], int, Tuple[int, int, int, int]]
_RectValue = Union[
    rect.Rect, Union[Tuple[int, int, int, int], Sequence[int]], Union[Tuple[_Coordinate, _Coordinate], Sequence[_Coordinate]],
]

def flip(surface: surface.Surface, xbool: bool, ybool: bool) -> surface.Surface: ...
def scale(
    surface: surface.Surface, size: Union[Tuple[int, int], Sequence[int]], dest_surface: Optional[surface.Surface] = ...,
) -> surface.Surface: ...
def rotate(surface: surface.Surface, angle: float) -> surface.Surface: ...
def rotozoom(surface: surface.Surface, angle: float, scale: float) -> surface.Surface: ...
def scale2x(surface: surface.Surface, dest_surface: Optional[surface.Surface] = ...) -> surface.Surface: ...
def smoothscale(
    surface: surface.Surface, size: Union[Tuple[int, int], Sequence[int]], dest_surface: Optional[surface.Surface] = ...,
) -> surface.Surface: ...
def get_smoothscale_backend() -> str: ...
def set_smoothscale_backend(value: str) -> None: ...
def chop(surface: surface.Surface, rect: _RectValue) -> surface.Surface: ...
def laplacian(surface: surface.Surface, dest_surface: surface.Surface) -> surface.Surface: ...
def average_surfaces(
    surfaces: Sequence[surface.Surface],
    dest_surface: Optional[surface.Surface] = ...,
    palette_colors: Optional[Union[bool, int]] = ...,
) -> surface.Surface: ...
def average_color(surface: surface.Surface, rect: Optional[_RectValue]) -> color.Color: ...
def threshold(
    dest_surface: surface.Surface,
    surf: surface.Surface,
    search_color: _ColorValue,
    threshold: Optional[_ColorValue] = ...,
    set_color: Optional[_ColorValue] = ...,
    set_behavior: Optional[int] = ...,
    search_surf: Optional[surface.Surface] = ...,
    inverse_set: Optional[bool] = ...,
) -> int: ...
