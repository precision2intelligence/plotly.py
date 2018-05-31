import _plotly_utils.basevalidators


class OpacitysrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='opacitysrc',
        parent_name='scattercarpet.marker',
        **kwargs
    ):
        super(OpacitysrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )