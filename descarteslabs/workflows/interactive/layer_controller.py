import weakref

import ipyleaflet
import ipywidgets as widgets
import traitlets

from .layer import WorkflowsLayer
from .layer_controller_row import LayerControllerRow
from .map_ import Map


class LayerControllerList(widgets.VBox):
    """
    Widget displaying a list of `LayerControllerRow` widgets for a `Map`.

    Example
    -------
    >>> import descarteslabs.workflows as wf
    >>> my_map = wf.Map() # doctest: +SKIP
    >>> img = wf.Image.from_id("landsat:LC08:PRE:TOAR:meta_LC80330352016022_v1").pick_bands("red") # doctest: +SKIP
    >>> img.visualize("sample visualization", map=my_map) # doctest: +SKIP
    >>> my_map # doctest: +SKIP
    >>> # ^ shows map with no layer controls
    >>> layer_controller = wf.interactive.LayerControllerList(my_map) # doctest: +SKIP
    >>> layer_controller # doctest: +SKIP
    >>> # ^ shows layer controls as a separate widget
    >>> layer_controller.children # doctest: +SKIP
    >>> # ^ list of individual widgets controlling each layer
    """
    map = traitlets.Instance(Map, help="The map being controlled")

    def __init__(self, map):
        super(LayerControllerList, self).__init__()

        self.map = map
        self._controllers_by_id = weakref.WeakValueDictionary()

        map.observe(self._layers_changed, names=["layers"])

        self._layers_changed({"old": [], "new": map.layers})
        # initialize with the current layers on the map, if any

        self.layout.overflow = "auto"
        self.layout.max_height = "12rem"
        self.layout.flex = "0 0 auto"

    def _layers_changed(self, change):
        new_layers = change["new"]
        controllers = []

        for layer in new_layers:
            if isinstance(layer, WorkflowsLayer):
                try:
                    controller = self._controllers_by_id[layer.model_id]
                except KeyError:
                    controller = LayerControllerRow(layer, self.map)
                    self._controllers_by_id[layer.model_id] = controller

                controllers.append(controller)

        self.children = tuple(reversed(controllers))


class LayerController(ipyleaflet.WidgetControl):
    """
    An ``ipyleaflet.WidgetControl`` for managing `WorkflowsLayer`.

    Unlike other ipyleaflet controls, a `Map` must be passed in on instantiation.
    Creating a `LayerController` automatically adds it to the given Map.

    Example
    -------
    >>> import descarteslabs.workflows as wf
    >>> img = wf.Image.from_id("landsat:LC08:PRE:TOAR:meta_LC80330352016022_v1").pick_bands("red green blue")
    >>> my_map = wf.Map()  # doctest: +SKIP
    >>> layer = wf.WorkflowsLayer(img)  # doctest: +SKIP
    >>> my_map.add_layer(layer)  # doctest: +SKIP
    >>> ctl = wf.LayerController(my_map)  # doctest: +SKIP
    >>> my_map  # doctest: +SKIP

    Attributes
    ----------
    controller_list: LayerControllerList
        The `LayerControllerList` widget displayed.
    """

    def __init__(self, map, **kwargs):
        """
        Create the LayerController.

        Parameters
        ----------
        map: Map
            The `Map` to which to add this control.
        """
        self.controller_list = LayerControllerList(map)
        accordion = widgets.Accordion(children=[self.controller_list])
        accordion.set_title(0, "Layers")

        super(LayerController, self).__init__(widget=accordion, **kwargs)

        map.add_control(self)
