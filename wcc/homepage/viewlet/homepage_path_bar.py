from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.viewlets import interfaces as manager
from wcc.homepage.interfaces import IProductSpecific
from wcc.homepage.interfaces import IBaseHomepage
grok.templatedir('templates')

class HomepagePathBar(grok.Viewlet):
    grok.context(IBaseHomepage)
    grok.viewletmanager(manager.IAboveContent)
    grok.name('plone.path_bar')
    grok.layer(IProductSpecific)

    def available(self):
        return True

    def render(self):
        return u''
