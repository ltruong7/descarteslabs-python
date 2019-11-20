import six

from ..containers import Dict, List
from ..core import typecheck_promote
from ..primitives import Float, Int, Str
from ..function import Function

try:
    # only after py3.4
    from collections import abc
except ImportError:
    import collections as abc


class BandsMixin:
    def __init__(self):
        raise TypeError("Please use Image or ImageCollection.")

    def pick_bands(self, bands):
        """
        New `Image`, containing only the given bands.

        Bands can be given as a sequence of strings,
        or a single space-separated string (like ``"red green blue"``).

        Bands on the new `Image` will be in the order given.
        """
        namespace = type(self).__name__
        if isinstance(bands, abc.Sequence):
            # Allows for a cleaner graft for this common use-case.
            # Note that both strings and normal lists/tuples are Sequences.
            if isinstance(bands, six.string_types):
                bands = bands.split()
            else:
                if not all(
                    isinstance(band, six.string_types + (Str,)) for band in bands
                ):
                    raise TypeError(
                        "Band names must all be strings, not {!r}".format(bands)
                    )
            return self._from_apply("{}.pick_bands".format(namespace), self, *bands)
        else:
            return self._pick_bands_list(bands)

    @typecheck_promote(List[Str])
    def _pick_bands_list(self, bands):
        namespace = type(self).__name__
        return self._from_apply("{}.pick_bands_list".format(namespace), self, bands)

    def unpack_bands(self, bands):
        """
        Convenience method for unpacking multiple bands into Python variables.

        Returns a Python tuple of ``self.pick_bands`` called for each band name.
        Bands can be given as a space-separated string of band names, or a sequence.

        Example
        -------
        >>> import descarteslabs.workflows as wf
        >>> img = wf.Image.from_id("sentinel-2:L1C:2019-05-04_13SDV_99_S2B_v1")
        >>> red, green, blue = img.unpack_bands("red green blue")
        """
        if isinstance(bands, six.string_types):
            bands = bands.split()
        if len(bands) == 1:
            return self.pick_bands(bands[0])
        else:
            return tuple(self.pick_bands(band) for band in bands)

    def rename_bands(self, *new_positional_names, **new_names):
        """
        New `Image`, with bands renamed by position or name.

        New names can be given positionally (like ``rename_bands('new_red', 'new_green')``),
        which renames the i-th band to the i-th argument.

        Or, new names can be given by keywords (like ``rename_bands(red="new_red")``)
        mapping from old band names to new ones.

        To eliminate ambiguity, names cannot be given both ways.
        """
        if len(new_positional_names) > 0 and len(new_names) > 0:
            raise TypeError(
                "New band names cannot be given both positionally and by name, "
                "due to potential ambiguity. Please separate this into two calls."
            )
        if len(new_positional_names) > 0:
            return self._rename_bands_positionally(new_positional_names)
        else:
            return self._rename_bands(new_names)

    @typecheck_promote(Dict[Str, Str])
    def _rename_bands(self, new_names):
        namespace = type(self).__name__
        return self._from_apply("{}.rename_bands".format(namespace), self, new_names)

    @typecheck_promote(List[Str])
    def _rename_bands_positionally(self, new_positional_names):
        namespace = type(self).__name__
        return self._from_apply(
            "{}.rename_bands_positionally".format(namespace), self, new_positional_names
        )

    def map_bands(self, func):
        """
        Map a function over each band in ``self``.

        The function must take 2 arguments:

            1. `Str`: the band name
            2. `Image`: 1-band `Image`

        If the function returns an `Image`, `map_bands` will also
        return one `Image`, containing the bands from all Images
        returned by ``func`` concatenated together.

        Otherwise, `map_bands` will return a `Dict` of the results
        of each call to ``func``, where the keys are the band names.

        Note that ``func`` can return Images with more than 1 band,
        but the band names must be unique across all of its results.

        Parameters
        ----------
        func: Python function
            Function that takes a `Str` and an `Image`.

        Returns
        -------
        `Image` if ``func`` returns `Image`, otherwise ``Dict[Str, T]``,
        where ``T`` is the return type of ``func``.
        """
        self_type = type(self)

        delayed_func = Function._delay(func, None, Str, self_type)
        result_type = type(delayed_func)

        if result_type is not self_type:
            result_type = Dict[Str, result_type]

        return result_type._from_apply("map_bands", self, delayed_func)


class GeometryMixin:
    @typecheck_promote((Int, Float))
    def buffer(self, distance):
        return self._from_apply("buffer", self, distance)
