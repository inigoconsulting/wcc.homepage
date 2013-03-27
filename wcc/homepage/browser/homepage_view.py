from five import grok
from plone.directives import dexterity, form
from wcc.homepage.content.homepage import IHomepage

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IHomepage)
    grok.require('zope2.View')
    grok.template('homepage_view')
    grok.name('view')

