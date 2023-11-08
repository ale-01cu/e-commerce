from django.db import models
from simple_history.models import HistoricalRecords
from .actions import generate_product_photo_path, generate_product_images_path
from apps.category.models import Category
from django.utils import timezone


class Measure_unit(models.Model):
    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medidas"

    name = models.CharField(unique=True, max_length=255, verbose_name="Nombre")

    symbol = models.CharField(
        unique=True, max_length=5, verbose_name="Simbolo de medida"
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    name = models.CharField(
        unique=True, max_length=255, verbose_name="Nombre de la marca"
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        
    name = models.CharField(unique=True, max_length=255, verbose_name="Nombre")

    photo = models.ImageField(
        verbose_name="Foto", upload_to=generate_product_photo_path
    )

    description = models.TextField(verbose_name="Descripcion")

    price = models.FloatField(verbose_name="Precio")

    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="product", verbose_name="Marca"
    )

    stock = models.PositiveIntegerField(default=0, verbose_name="Cantidad")

    keywords = models.CharField(max_length=255, verbose_name="Palabras claves")

    category = models.ForeignKey(
        Category,
        related_name="Products",
        on_delete=models.CASCADE,
        verbose_name="Categoria",
    )

    measure_unit = models.ForeignKey(
        Measure_unit,
        related_name="Product",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Unidad de medida",
    )

    create_date = models.DateTimeField(
        verbose_name="Fecha de creado", auto_now_add=True
    )

    status = models.BooleanField(default=True, verbose_name="Estado")

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def get_offers(self):  # Obtiene ka oferta del producto
        from apps.offers.models import OfferProduct

        now = timezone.now()

        return OfferProduct.objects.filter(
            product=self,
            offer__status=True,
            offer__start_date__lte=now,
            offer__end_date__gte=now,
        ).first()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    @property
    def rating(self):  # Calcula la valoracion del producto a partir de sus comentarios
        from apps.comments.models import Comments
        from django.db.models import Avg

        rating_average = Comments.objects.filter(product=self).aggregate(Avg("rating"))

        rounded_rating_average = 0
        if rating_average["rating__avg"] is not None:
            rounded_rating_average = round(rating_average["rating__avg"], 1)

        return rounded_rating_average

    @property
    def discount_price(
        self,
    ):  # Calcula el descuento del producto a partir de sus ofertas
        offer = self.get_offers()

        if offer:
            if offer.discount_type == "$":
                if offer.discount < self.price:
                    return self.price - offer.discount

                return 0
            else:
                discount = (offer.discount * self.price) / 100
                return self.price - discount
        else:
            return 0


class Image(models.Model):
    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"

    image = models.ImageField(
        unique=True,
        verbose_name="Url de la Imagen",
        upload_to=generate_product_images_path,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="Images",
        verbose_name="Prodduto",
    )

    def __str__(self):
        return str(self.image)
