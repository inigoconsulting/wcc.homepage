from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent

from wcc.homepage import MessageFactory as _
from wcc.carousel.interfaces import ICarouselImageEnabled
from wcc.homepage.interfaces import IBaseHomepage

from Products.ATContentTypes.interfaces.topic import IATTopic
from plone.app.collection.interfaces import ICollection

# Interface class; used to define content-type schema.

class IHomepage3(form.Schema, IBaseHomepage, IImageScaleTraversable):
    """
    
    """
    languageindependent('slider_items')
    slider_items = RelationList(
        title=u'Slider items',
        value_type=RelationChoice(
            source=ObjPathSourceBinder(
                object_provides=ICarouselImageEnabled.__identifier__
            )
        ),
        required=True
    )

    languageindependent('news_source')
    news_source = RelationChoice(
        title=u'Source collection for news listing',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                            ICollection.__identifier__]
        ),
        required=False
    )

    languageindependent('more_news_target')
    more_news_target = RelationChoice(
        title=u'Target for "More News" link',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                            ICollection.__identifier__]
        ),
        required=False,
    )

    form.widget(third_column_text="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    third_column_text = schema.Text(
        title=u"Third Column Text",
        description=u'',
        required=False,
    )
