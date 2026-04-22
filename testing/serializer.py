from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    mini_price = serializers.FloatField(required=False,min_value=0)
    max_price = serializers.FloatField(required=False,min_value=0)
    category = serializers.CharField(required=False)


    def validate(self,data):
        mini_price = data.get("mini_price")
        max_price = data.get("max_price")
        if mini_price and max_price and mini_price > max_price:
            raise serializers.ValidationError(
                "minimum price should not be greater than maximum price"
            )
        return data

class ProductResponseSerializer(serializers.Serializer):

    total_product = serializers.IntegerField()
    average_price = serializers.FloatField()
    total_stock_value = serializers.FloatField()