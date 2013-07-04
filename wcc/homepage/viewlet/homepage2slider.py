from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.viewlets import interfaces as manager
from wcc.homepage.interfaces import IProductSpecific
from wcc.homepage.content.homepage2 import IHomepage2
from wcc.homepage.browser.homepage2_view import Index
from Products.ContentWellPortlets.browser.interfaces import IHeaderPortlets

grok.templatedir('templates')

class Homepage2Slider(grok.Viewlet):
    grok.context(IHomepage2)
    grok.view(Index)
    grok.viewletmanager(manager.IPortalTop)
    grok.template('homepage2slider')
    grok.layer(IProductSpecific)

    def available(self):
        return True

    def slider_items(self):
        if not self.context.slider_items:
            return []
        return [i.to_object for i in self.context.slider_items]

    def get_image_tag(self, obj):
        scales = obj.restrictedTraverse('@@images')
        image = scales.scale('carousel_image', width=782, height=330)
        placeholder = '<img src="http://placehold.it/782x330"/>'
        if not image:
            return placeholder
        return image.tag()
