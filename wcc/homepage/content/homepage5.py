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
from ftw.blog.interfaces import IBlog
from collective.sliderfields.interfaces import ISliderFieldsEnabled

# Interface class; used to define content-type schema.

class IHomepage5(form.Schema, IBaseHomepage, IImageScaleTraversable):
    """
    Description of the Example Type
    """

    languageindependent('slider_items')
    slider_items = RelationList(
        title=u'Slider items',
        value_type=RelationChoice(
            source=ObjPathSourceBinder(
                object_provides=ISliderFieldsEnabled.__identifier__
            )
        ),
        required=True
    )

    languageindependent('source1')
    source1 = RelationChoice(
        title=u'Source collection row1',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                            ICollection.__identifier__]
        ),
        required=False
    )

    source1_text = RichText(
        title=_(u'Text for row1'),
        description=_(u''),
        required=False
    )


    languageindependent('source2')
    source2 = RelationChoice(
        title=u'Source collection for row2',
        source=ObjPathSourceBinder(
            object_provides=[IATTopic.__identifier__,
                            ICollection.__identifier__]
        ),
        required=False
    )

    source2_text = RichText(
        title=_(u'Text for row2'),
        description=_(u''),
        required=False
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
