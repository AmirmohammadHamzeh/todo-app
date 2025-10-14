from rest_framework import serializers
from .models import Todo, Label


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name']


class TodoSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)  # نمایش کامل لیبل‌ها
    label_ids = serializers.ListField(
        write_only=True,
        child=serializers.IntegerField(),
        required=False
    )  # برای ارسال آیدی‌ها هنگام create/update

    class Meta:
        model = Todo
        fields = [
            'id', 'title', 'description', 'is_completed', 'priority',
            'labels', 'label_ids', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        label_ids = validated_data.pop('label_ids', [])
        user = self.context['request'].user
        todo = Todo.objects.create(user=user, **validated_data)
        if label_ids:
            todo.labels.set(Label.objects.filter(id__in=label_ids))
        return todo

    def update(self, instance, validated_data):
        label_ids = validated_data.pop('label_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if label_ids is not None:
            instance.labels.set(Label.objects.filter(id__in=label_ids))
        return instance
