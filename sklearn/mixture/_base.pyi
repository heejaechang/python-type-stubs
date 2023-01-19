from numpy import float64, ndarray
from typing import Optional, Tuple, Union, Any
from numpy.typing import ArrayLike, NDArray

# Author: Wei Xue <xuewei4d@gmail.com>
# Modified by Thierry Guillemot <thierry.guillemot.work@gmail.com>
# License: BSD 3 clause

import numbers
import warnings
from abc import ABCMeta, abstractmethod
from time import time

import numpy as np
from scipy.special import logsumexp

from .. import cluster
from ..cluster import kmeans_plusplus
from ..base import BaseEstimator
from ..base import DensityMixin
from ..exceptions import ConvergenceWarning
from ..utils import check_random_state, check_scalar
from ..utils.validation import check_is_fitted
from numpy.random.mtrand import RandomState
from numpy.random import RandomState
from sklearn.mixture._bayesian_mixture import BayesianGaussianMixture
from sklearn.mixture._gaussian_mixture import GaussianMixture

def _check_shape(param: ndarray, param_shape: Tuple[int, int], name: str) -> None: ...

class BaseMixture(DensityMixin, BaseEstimator, metaclass=ABCMeta):
    def __init__(
        self,
        n_components: int,
        tol: float,
        reg_covar: Union[int, float],
        max_iter: int,
        n_init: int,
        init_params: str,
        random_state: Optional[Union[RandomState, int]],
        warm_start: bool,
        verbose: int,
        verbose_interval: int,
    ) -> None: ...
    def _check_initial_parameters(self, X: ndarray) -> None: ...
    @abstractmethod
    def _check_parameters(self, X): ...
    def _initialize_parameters(self, X: ndarray, random_state: RandomState) -> None: ...
    @abstractmethod
    def _initialize(self, X, resp): ...
    def fit(self, X: ArrayLike, y: None = None) -> Union[BayesianGaussianMixture, GaussianMixture]: ...
    def fit_predict(self, X: ArrayLike, y: None = None) -> NDArray: ...
    def _e_step(self, X: ndarray) -> Tuple[float64, ndarray]: ...
    @abstractmethod
    def _m_step(self, X, log_resp): ...
    @abstractmethod
    def _get_parameters(self): ...
    @abstractmethod
    def _set_parameters(self, params): ...
    def score_samples(self, X: ArrayLike) -> NDArray: ...
    def score(self, X: ArrayLike, y: None = None) -> float: ...
    def predict(self, X: ArrayLike) -> NDArray: ...
    def predict_proba(self, X: ArrayLike) -> NDArray: ...
    def sample(self, n_samples: int = 1) -> tuple[NDArray, NDArray]: ...
    def _estimate_weighted_log_prob(self, X: ndarray) -> ndarray: ...
    @abstractmethod
    def _estimate_log_weights(self): ...
    @abstractmethod
    def _estimate_log_prob(self, X): ...
    def _estimate_log_prob_resp(self, X: ndarray) -> Tuple[ndarray, ndarray]: ...
    def _print_verbose_msg_init_beg(self, n_init: int) -> None: ...
    def _print_verbose_msg_iter_end(self, n_iter: int, diff_ll: float64) -> None: ...
    def _print_verbose_msg_init_end(self, ll: float64) -> None: ...