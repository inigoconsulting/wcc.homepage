from five import grok
from plone.directives import dexterity, form
from wcc.homepage.content.homepage5 import IHomepage5
from plone.api.portal import get_localized_time
import re

grok.templatedir('templates')


class Index(dexterity.DisplayForm):
    grok.context(IHomepage5)
    grok.require('zope2.View')
    grok.template('homepage5_view')
    grok.name('view')

    def slider_items(self):
        if not self.context.slider_items:
            return []
        return [i.to_object for i in self.context.slider_items]

    def source1_items(self):
        rel = self.context.source1
        if not rel:
            return []
        source = rel.to_object
        results = source.queryCatalog(batch=False) or []
        return [i.getObject() for i in results[:3]]

    def source2_items(self):
        rel = self.context.source2
        if not rel:
            return []
        source = rel.to_object
        results = source.queryCatalog(batch=False) or []
        return [i.getObject() for i in results[:3]]

    def blog_items(self):
        rel = self.context.blog_source
        if not rel:
            return []
        source = rel.to_object
        results = source.queryCatalog(batch=False) or []
        return [i.getObject() for i in results[:3]]


    def get_image_tag(self, obj):
        scales = obj.restrictedTraverse('@@images')
        if self.context.slider_type == 'full-width':
            image = scales.scale('carousel_image', width=782, height=330)
            placeholder = '<img src="http://placehold.it/782x330"/>'
        else:
            image = scales.scale('carousel_image', width=510, height=330)
            placeholder = '<img src="http://placehold.it/510x330"/>'
        if not image:
            return placeholder
        return image.tag()

    def slider_slide_style(self):
        if self.context.slider_type == 'full-width':
            return "width:782px;height:330px;padding:5px 10px;"
        return "width:510px;height:330px;padding:5px 10px;"

    def slider_style(self):
        if self.context.slider_type == 'full-width':
            return "width:1060px;"
        return "width:790px"

    def homepage_class(self):
        if self.context.slider_type == 'full-width':
            return 'homepage-full-width homepage-view'
        return 'homepage-normal-width homepage-view'

    def slider_slide_wrap_inner_style(self):
        if self.context.slider_type == 'full-width':
            return "width:782px;height:330px;"
        return "width:510px;height:330px;"


class HomepageJS(grok.View):
    grok.context(IHomepage5)
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

        if self.context.slider_type == 'full-width':
            return template % {'width': 782, 'height': 330}
        return  template % {'width': 510, 'height': 330}

