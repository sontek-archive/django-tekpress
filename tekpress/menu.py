from django.core.urlresolvers import reverse
from admin_tools.menu import items, Menu
from django.conf import settings

class MyMenu(Menu):
    def __init__(self, **kwargs):
        super(MyMenu, self).__init__(**kwargs)
        self.children.append(
            items.MenuItem(title='Home', url=reverse('admin:index'))
        )
        self.children.append(
            items.AppList(title='Applications')
        )
        self.children.append(
            items.MenuItem(title='Photos', url=reverse('fb_browse'))
        )
        self.children.append(
            items.MenuItem(title='New Blog Post', url=reverse('admin:tekblog_entry_add'))
        )

        self.children.append(
            items.MenuItem(
                title='Quick Links',
                children=[
                    items.MenuItem(title='View site', url='/'),
                    items.MenuItem(title='Change password', url=reverse('admin:password_change')),
                    items.MenuItem(title='Sign out', url=settings.LOGOUT_URL),
                ]
            )
        )
