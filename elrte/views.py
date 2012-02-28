from pyramid.view import view_config

import tw2.jqplugins.elrte

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'widget': tw2.jqplugins.elrte.elRTEWidget(id='foo')}
