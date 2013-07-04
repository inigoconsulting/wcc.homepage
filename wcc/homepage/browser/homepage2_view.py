from five import grok
from plone.directives import dexterity, form
from wcc.homepage.content.homepage2 import IHomepage2

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IHomepage2)
    grok.require('zope2.View')
    grok.template('homepage2_view')
    grok.name('view')

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


class HomepageJS(grok.View):
    grok.context(IHomepage2)
    grok.name('homepage.js')

    def render(self):
        self.request.response.setHeader('Content-Type', 'text/javascript')
        template = '''
var homepageJQ = $.noConflict();
homepageJQ(document).ready(function() {
    homepageJQ("#homepage-slider").lofJSidernews({ interval:5000,
        easing:'easeInOutQuad',
        duration:600,
        direction: 'opacity',
        auto:true,
        mainWidth:%(width)s,
        mainHeight:%(height)s,
        navigatorHeight : 87,
        navigatorWidth : 303,
        maxItemDisplay:4,
        navigatorEvent: 'mouseenter'
    });
})
        '''

        return template % {'width': 782, 'height': 330}
