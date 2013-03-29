from five import grok
from plone.directives import dexterity, form
from wcc.homepage.content.homepage import IHomepage

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IHomepage)
    grok.require('zope2.View')
    grok.template('homepage_view')
    grok.name('view')

    def slider_items(self):
        if not self.context.slider_items:
            return []
        return [i.to_object for i in self.context.slider_items]

    def news_items(self):
        rel = self.context.news_source
        if not rel:
            return []
        source = rel.to_object
        results = source.queryCatalog(batch=False) or []
        return [i.getObject() for i in results[:3]]

    def event_items(self):
        rel = self.context.events_source
        if not rel:
            return []
        source = rel.to_object
        results = source.queryCatalog(batch=False) or []
        return [i.getObject() for i in results[:5]]

    def more_news_target(self):
        if self.context.more_news_target:
            return self.context.more_news_target.to_object
        return self.context.news_source.to_object

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
            return "width:1062px;" # 782 + 272
        return "width:790px" # 510 + 272

    def homepage_class(self):
        if self.context.slider_type == 'full-width':
            return 'homepage-full-width'
        return 'homepage-normal-width'

class HomepageJS(grok.View):
    grok.context(IHomepage)
    grok.name('homepage.js')

    def render(self):
        self.request.response.setHeader('Content-Type', 'text/javascript')
        template = '''
var homepageJQ = $.noConflict();
homepageJQ(document).ready(function() {
    homepageJQ("#homepage-slider").lofJSidernews({ interval:5000,
        easing:'easeInOutQuad',
        duration:1200,
        auto:true,
        mainWidth:%(width)s,
        mainHeight:%(height)s,
        navigatorHeight : 87,
        navigatorWidth : 303,
        maxItemDisplay:4
    });
})
        '''

        if self.context.slider_type == 'full-width':
            return template % {'width': 782, 'height': 330}
        return  template % {'width': 510, 'height': 330}

