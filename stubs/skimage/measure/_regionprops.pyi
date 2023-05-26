from skimage.measure._regionprops import RegionProperties
from numpy.typing import ArrayLike
from typing import Mapping
import inspect
from functools import wraps
from math import atan2
from math import pi as PI
from math import sqrt
from warnings import warn

import numpy as np
from scipy import ndimage as ndi
from scipy.spatial.distance import pdist

from . import _moments
from ._find_contours import find_contours
from ._marching_cubes_lewiner import marching_cubes
from ._regionprops_utils import euler_number, perimeter, perimeter_crofton

__all__ = ["regionprops", "euler_number", "perimeter", "perimeter_crofton"]

# All values in this PROPS dict correspond to current scikit-image property
# names. The keys in this PROPS dict correspond to older names used in prior
# releases. For backwards compatibility, these older names will continue to
# work, but will not be documented.
PROPS: dict = ...

OBJECT_COLUMNS: set = ...

COL_DTYPES: dict = ...

PROP_VALS = ...

def _infer_number_of_required_args(func): ...
def _infer_regionprop_dtype(func, *, intensity, ndim): ...
def _cached(f): ...
def only2d(method): ...
def _inertia_eigvals_to_axes_lengths_3D(inertia_tensor_eigvals): ...

class RegionProperties:
    def __init__(
        self,
        slice,
        label,
        label_image,
        intensity_image,
        cache_active,
        *,
        extra_properties=None
    ): ...
    def __getattr__(self, attr): ...
    def __setattr__(self, name, value): ...
    @property
    @_cached
    def area(self): ...
    @property
    def bbox(self): ...
    @property
    def area_bbox(self): ...
    @property
    def centroid(self): ...
    @property
    @_cached
    def area_convex(self): ...
    @property
    @_cached
    def image_convex(self): ...
    @property
    def coords(self): ...
    @property
    @only2d
    def eccentricity(self): ...
    @property
    def equivalent_diameter_area(self): ...
    @property
    def euler_number(self): ...
    @property
    def extent(self): ...
    @property
    def feret_diameter_max(self): ...
    @property
    def area_filled(self): ...
    @property
    @_cached
    def image_filled(self): ...
    @property
    @_cached
    def image(self): ...
    @property
    @_cached
    def inertia_tensor(self): ...
    @property
    @_cached
    def inertia_tensor_eigvals(self): ...
    @property
    @_cached
    def image_intensity(self): ...
    def _image_intensity_double(self): ...
    @property
    def centroid_local(self): ...
    @property
    def intensity_max(self): ...
    @property
    def intensity_mean(self): ...
    @property
    def intensity_min(self): ...
    @property
    def axis_major_length(self): ...
    @property
    def axis_minor_length(self): ...
    @property
    @_cached
    def moments(self): ...
    @property
    @_cached
    def moments_central(self): ...
    @property
    @only2d
    def moments_hu(self): ...
    @property
    @_cached
    def moments_normalized(self): ...
    @property
    @only2d
    def orientation(self): ...
    @property
    @only2d
    def perimeter(self): ...
    @property
    @only2d
    def perimeter_crofton(self): ...
    @property
    def solidity(self): ...
    @property
    def centroid_weighted(self): ...
    @property
    def centroid_weighted_local(self): ...
    @property
    @_cached
    def moments_weighted(self): ...
    @property
    @_cached
    def moments_weighted_central(self): ...
    @property
    @only2d
    def moments_weighted_hu(self): ...
    @property
    @_cached
    def moments_weighted_normalized(self): ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def __eq__(self, other): ...

# For compatibility with code written prior to 0.16
_RegionProperties = RegionProperties

def _props_to_dict(regions, properties=("label", "bbox"), separator="-"): ...
def regionprops_table(
    label_image,
    intensity_image=None,
    properties: tuple | ArrayLike = ...,
    *,
    cache: bool = True,
    separator: str = "-",
    extra_properties=None
) -> Mapping: ...
def regionprops(
    label_image,
    intensity_image=None,
    cache: bool = True,
    coordinates=None,
    *,
    extra_properties=None
) -> list[RegionProperties]: ...
def _parse_docs(): ...
def _install_properties_docs(): ...