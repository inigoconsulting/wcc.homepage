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

from wcc.homepage import MessageFactory as _
from wcc.carousel.interfaces import ICarouselImageEnabled
from Products.ATContentTypes.interfaces.topic import IATTopic
from plone.app.collection.interfaces import ICollection

# Interface class; used to define content-type schema.

class IHomepage(form.Schema, IImageScaleTraversable):
    """
    Description of the Example Type
    """

    slider_items = RelationList(
        title=u'Slider items',
        value_type=RelationChoice(
            source=ObjPathSourceBinder(
                object_provides=ICarouselImageEnabled.__identifier__
            )
        ),
        required=True
    )

    news_source = RelationChoice(
        title=u'Source collection for news listing',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                            ICollection.__identifier__]
        ),
        required=True
    )

    more_news_target = RelationChoice(
        title=u'Target for "More News" link',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                            ICollection.__identifier__]
        ),
    )

    events_source = RelationChoice(
        title=u'Source collection for events listing',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                            ICollection.__identifier__]
        ),
        required=False
    )
