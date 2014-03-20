from collective.grok import gs
from Products.CMFCore.utils import getToolByName

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.homepage to 1002',
                description=u'Upgrade wcc.homepage to 1002',
                source='1001', destination='1002',
                sortkey=1, profile='wcc.homepage:default')
def to1002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.homepage.upgrades:to1002')


@gs.upgradestep(title=u'Upgrade wcc.homepage to 1001',
                description=u'Upgrade wcc.homepage to 1001',
                source='1', destination='1001',
                sortkey=1, profile='wcc.homepage:default')
def to1001(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.homepage.upgrades:to1001')
