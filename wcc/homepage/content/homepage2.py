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
from wcc.homepage.interfaces import IBaseHomepage
from collective import dexteritytextindexer
from wcc.carousel.interfaces import ICarouselImageEnabled

# Interface class; used to define content-type schema.

class IHomepage2(form.Schema, IBaseHomepage, IImageScaleTraversable):
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

    dexteritytextindexer.searchable('text')
    form.widget(text="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    text = schema.Text(
        title=_(u'label_body_text', u"Body Text"),
        description=u'',
        required=False,
    )
