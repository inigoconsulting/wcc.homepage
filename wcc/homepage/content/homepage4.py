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
from plone.multilingualbehavior.directives import languageindependent
from wcc.homepage.interfaces import IBaseHomepage

# Interface class; used to define content-type schema.

class IHomepage4(form.Schema, IBaseHomepage, IImageScaleTraversable):
    """
    Description of the Example Type
    """

#    languageindependent('slider_items')
    slider_items = RelationList(
        title=u'Slider items',
        value_type=RelationChoice(
            source=ObjPathSourceBinder(
                object_provides=ICarouselImageEnabled.__identifier__
            )
        ),
        required=True
    )

#    languageindependent('data_source')
    data_source = RelationChoice(
        title=u'Source collection for data',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                            ICollection.__identifier__]
        ),
        required=False
    )

#    languageindependent('more_data_target')
    more_data_target = RelationChoice(
        title=u'Target for "More" link',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                            ICollection.__identifier__]
        ),
        required=False,
    )

    languageindependent('slider_type')
    slider_type = schema.Choice(
        title=_(u'Slider type'),
        default='normal',
        values=['normal','full-width'],
        required=True,
        description=_(u'Normal slider requires 510x330px images, Full ' +
                    u'Width slider requires 782x330px images')
    )
