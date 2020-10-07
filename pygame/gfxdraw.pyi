# Portions (c) Microsoft Corporation

from typing import Sequence, Tuple, Union

from . import color, math, rect, surface

_ColorValue = Union[color.Color, Tuple[int, int, int], Sequence[int], int, Tuple[int, int, int, int]]
_RectValue = Union[rect.Rect, Tuple[int, int, int, int]]
_Coordinate = Union[Tuple[float, float], Sequence[float], math.Vector2]

def pixel(surface: surface.Surface, x: int, y: int, color: _ColorValue) -> None: ...
def hline(surface: surface.Surface, x1: int, x2: int, y: int, color: _ColorValue) -> None: ...
def vline(surface: surface.Surface, x: int, y1: int, y2: int, color: _ColorValue) -> None: ...
def line(surface: surface.Surface, x1: int, y1: int, x2: int, y2: int, color: _ColorValue) -> None: ...
def rectangle(surface: surface.Surface, rect: _RectValue, color: _ColorValue) -> None: ...
def box(surface: surface.Surface, rect: _RectValue, color: _ColorValue) -> None: ...
def circle(surface: surface.Surface, x: int, y: int, r: int, color: _ColorValue) -> None: ...
def aacircle(surface: surface.Surface, x: int, y: int, r: int, color: _ColorValue) -> None: ...
def filled_circle(surface: surface.Surface, x: int, y: int, r: int, color: _ColorValue) -> None: ...
def ellipse(surface: surface.Surface, x: int, y: int, rx: int, ry: int, color: _ColorValue) -> None: ...
def aaellipse(surface: surface.Surface, x: int, y: int, rx: int, ry: int, color: _ColorValue) -> None: ...
def filled_ellipse(surface: surface.Surface, x: int, y: int, rx: int, ry: int, color: _ColorValue) -> None: ...
def arc(surface: surface.Surface, x: int, y: int, r: int, start_angle: int, atp_angle: int, color: _ColorValue) -> None: ...
def pie(surface: surface.Surface, x: int, y: int, r: int, start_angle: int, atp_angle: int, color: _ColorValue) -> None: ...
def trigon(surface: surface.Surface, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, color: _ColorValue) -> None: ...
def aatrigon(surface: surface.Surface, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, color: _ColorValue) -> None: ...
def filled_trigon(surface: surface.Surface, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, color: _ColorValue) -> None: ...
def polygon(surface: surface.Surface, points: Sequence[_Coordinate], color: _ColorValue) -> None: ...
def aapolygon(surface: surface.Surface, points: Sequence[_Coordinate], color: _ColorValue) -> None: ...
def filled_polygon(surface: surface.Surface, points: Sequence[_Coordinate], color: _ColorValue) -> None: ...
def textured_polygon(
    surface: surface.Surface, points: Sequence[_Coordinate], texture: surface.Surface, tx: int, ty: int
) -> None: ...
def bezier(surface: surface.Surface, points: Sequence[_Coordinate], steps: int, color: _ColorValue) -> None: ...

