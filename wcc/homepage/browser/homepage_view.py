from five import grok
from plone.directives import dexterity, form
from wcc.homepage.content.homepage import IHomepage
from plone.api.portal import get_localized_time
import re

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IHomepage)
    grok.require('zope2.View')
    grok.template('homepage_view')
    grok.name('view')

    def slider_items(self):
        if not self.context.slider_items:
            return []
        return [i.to_object for i in self.context.slider_items if not i.isBroken()]

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
        return [i.getObject() for i in results[:7]]

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

    def get_event_date(self, obj):
        start = obj.startDate
        end = obj.endDate
        if start.year() == end.year():
            if start.month() == end.month():
                if start.day() == end.day():
                    return get_localized_time(start)
                else:
                    return u"{0} - {1}".format(
                        get_localized_time(start).split()[0],
                        get_localized_time(end))
            else:
                front_date = re.sub(str(start.year()), '',
                                    get_localized_time(start))
                return u"{0} - {1}".format(front_date, get_localized_time(end))

        return u'{0} - {1}'.format(get_localized_time(start),
                                  get_localized_time(end))

    def event_header_url(self):
        path = '#'
        if self.context.events_source:
            path = self.context.events_source.to_object.absolute_url()
        return path

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

