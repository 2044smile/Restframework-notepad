from rest_framework import serializers
from bbs.models import Bbs


class BbsSerializer(serializers.ModelSerializer):
    # Serializer 직렬화, 메모리상에 있는 변수와 값의 세트를 json 데이터로 변환해서 사용할 수 있게 된다.

    class Meta:
        fields = ['id', 'title', 'author', 'pw', 'content']

    # instance를 반환한다.
    def create(self, validated_data):
        return Bbs.objects.create(**validated_data)

    # 생성 된 instance를 리턴해준다.
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.pw = validated_data.get('pw', instance.pw)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
