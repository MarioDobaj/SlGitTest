from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class ContentPage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(blank=True)),
        ('image', ImageChooserBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(blank=True)
    image = ImageChooserBlock()
    description = blocks.CharBlock(blank=True)
    likes = blocks.IntegerBlock(blank=True)
    authorName = blocks.CharBlock(blank=True)

    class Meta:
        template = 'blocks/card_block.html'

class SingleCardBlock(blocks.StructBlock):
    title = blocks.CharBlock(blank=True)
    image = ImageChooserBlock()
    description = blocks.CharBlock(blank=True)
    likes = blocks.IntegerBlock(blank=True)
    authorName = blocks.CharBlock(blank=True)
    link = blocks.CharBlock(blank=True)
    price = blocks.CharBlock(blank=True)
    features = blocks.CharBlock(blank=True)

class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(SingleCardBlock(blank=True))

    class Meta:
        template = 'blocks/cards_block.html'
        icon = 'grip'
        label = 'Cards grid'

class ContentTestPage(Page):
    body = StreamField([
        ('text', blocks.RichTextBlock(blank=True)),
        ('cards', CardsBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    class Meta:
        template = 'blocks/image_block.html'
        icon = 'image'
        label = 'Image'

class VideoBlock(blocks.StructBlock):
    url = blocks.CharBlock()

    class Meta:
        template = 'blocks/video_block.html'
        icon = 'media'
        label = 'Youtube video'

class ContentTestPage2(Page):
    body = StreamField([
        ('text', blocks.RichTextBlock(blank=True)),
        ('cards', CardsBlock()),
        ('image', ImageBlock()),
        ('video', VideoBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

class HomePageNoHero(Page):
    body = StreamField([
        ('text', blocks.RichTextBlock(blank=True)),
        ('cards', CardsBlock()),
        ('image', ImageChooserBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

class HomePageHero(Page):
    title2 = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('title2', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('body', classname="full"),
    ]

class HomePageManual1(Page):
    title2 = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('title2', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('body', classname="full"),
    ]

class ActivityPage(Page):
    activityTitle = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    body = RichTextField(blank=True)
    price = models.CharField(max_length=255, blank=True)
    image1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image4 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    content_panels = Page.content_panels + [
        FieldPanel('activityTitle', classname="full"),
        FieldPanel('address', classname="full"),
        FieldPanel('price', classname="full"),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('image1'),
        ImageChooserPanel('image2'),
        ImageChooserPanel('image3'),
        ImageChooserPanel('image4'),
    ]


class ContentPageHero(Page):
    title2 = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('text', blocks.RichTextBlock(blank=True)),
        ('cards', CardsBlock()),
        ('image', ImageBlock()),
        ('video', VideoBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('title2', classname="full"),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]

class ContentPageNoHero(Page):
    body = StreamField([
        ('text', blocks.RichTextBlock(blank=True)),
        ('cards', CardsBlock()),
        ('image', ImageBlock()),
        ('video', VideoBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]