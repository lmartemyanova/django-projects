from rest_framework import serializers

from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for p in positions:
            product, quantity, price = p['product'], p['quantity'], p['price']
            StockProduct.objects.create(stock_id=stock.id,
                                        product_id=product.id,
                                        quantity=quantity,
                                        price=price)
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        if positions:
            for p in positions:
                product, quantity, price = p['product'], p['quantity'], p['price']

                obj, created = StockProduct.objects.update_or_create(product_id=product.id,
                                                                     defaults={'stock_id': stock.id,
                                                                               'quantity': quantity,
                                                                               'price': price})
                print(obj, created)

        return stock
