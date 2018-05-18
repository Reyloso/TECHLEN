from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class SuitConfig(DjangoSuitConfig):
    #layout = 'horizontal'
    name = 'suit'
    verbose_name = 'Django Suit'
    # Menu and header layout - horizontal or vertical
    layout = 'horizontal'

    # Set default list per page
    list_per_page = 20

    # Show changelist top actions only if any row is selected
    toggle_changelist_top_actions = True

    # Define menu
    #: :type: list of suit.menu.ParentItem
    menu = (

        ParentItem('Configuracion', children=[
            ChildItem(model='configuracion.programa'),
            ChildItem(model='configuracion.cargo'),
            ChildItem(model='configuracion.dependencia'),
        ]),
        ParentItem('Personas', children=[
            ChildItem(model='personas.personas'),
        ]),
        ParentItem('Prestamos', children=[
            ChildItem(model='prestamos.prestamo'),
            ChildItem(model='prestamos.incidente'),
            ChildItem('Prestar ', url='/admin/Prestamo/Prestar/'),
        ]),
        ParentItem('Recursos', children=[
            ChildItem(model='recursos.recurso'),
            ChildItem(model='recursos.tipo_recurso'),
        ]),
        ParentItem('Gestion de usuario', children=[
            ChildItem(model='auth.user'),
            ChildItem(model='auth.group')
        ]),

    )
