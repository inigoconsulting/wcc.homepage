from five import grok
from plone.directives import dexterity, form
from wcc.homepage.content.homepage4 import IHomepage4

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IHomepage4)
    grok.require('zope2.View')
    grok.template('homepage4_view')
    grok.name('view')

