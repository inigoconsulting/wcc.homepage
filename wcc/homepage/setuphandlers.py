from collective.grok import gs
from wcc.homepage import MessageFactory as _

@gs.importstep(
    name=u'wcc.homepage', 
    title=_('wcc.homepage import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.homepage.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
