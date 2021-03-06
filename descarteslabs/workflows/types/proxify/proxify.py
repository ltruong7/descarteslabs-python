import datetime


def proxify(obj):
    from ..core import Proxytype, ProxyTypeError
    from ..function import Function
    from ..containers import Tuple, List
    from ..primitives import Int, Float, Bool, Str, NoneType, Any
    from ..datetimes import Datetime, Timedelta

    if isinstance(obj, Proxytype):
        return obj
    elif callable(obj):
        return Function.from_callable(obj)
    elif isinstance(obj, (tuple, list)):
        contents = [proxify(x) for x in obj]
        types = tuple(type(x) for x in contents)
        if (
            isinstance(obj, list)
            and len(types) > 0
            and all(t is types[0] for t in types[1:])
        ):
            return List[types[0]](contents)
        else:
            return Tuple[types](contents)
    elif isinstance(obj, bool):
        return Bool(obj)
    elif isinstance(obj, int):
        return Int(obj)
    elif isinstance(obj, float):
        return Float(obj)
    elif isinstance(obj, str):
        return Str(obj)
    elif obj is None:
        return NoneType(obj)
    elif isinstance(obj, (datetime.datetime, datetime.date)):
        return Datetime._promote(obj)
    elif isinstance(obj, datetime.timedelta):
        return Timedelta._promote(obj)
    else:
        try:
            return Any._promote(obj)
        except ProxyTypeError:
            raise NotImplementedError(
                "Cannot automatically convert to a Proxytype. "
                "Please manually construct the appropriate container type "
                "and initialize it with your object. Value: {!r}".format(obj)
            )
