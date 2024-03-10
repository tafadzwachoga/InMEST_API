from rest_framework import serializers

class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()


class CohortSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    year = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    is_active = serializers.BooleanField()
    author = UserSerializer(many=False)


class CohortMemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    member = serializers.IntegerField()
    is_active = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()
    author = UserSerializer(many=False)
    