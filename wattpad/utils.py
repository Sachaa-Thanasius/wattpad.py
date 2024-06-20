from collections.abc import Sequence
from typing import Union

from yarl import URL


class Route:
    """A helper class for instantiating an HTTP method to Wattpad. Implementation inspired by Hondana.

    Parameters
    ----------
    verb : :class:`str`
        The HTTP method to perform, e.g. ``GET``.
    base : :class:`str`
        The base URL for the API, e.g. "https://api.wattpad.com".
    path : :class:`str`
        The path for the API endpoint to target, e.g. ``/stories/{story_id}``
    params : Mapping


    References
    ----------
    https://github.com/AbstractUmbra/Hondana/blob/main/hondana/utils.py#L134

    """

    def __init__(
        self,
        verb: str,
        base: str,
        path: str,
        **params: Union[str, int, float, Sequence[Union[str, int, float]]],  # noqa: PYI041
    ) -> None:
        self.verb = verb
        self.base = base
        self.path = path
        self.url = URL.build(scheme="https", host=self.base, path=self.path, query=params)
