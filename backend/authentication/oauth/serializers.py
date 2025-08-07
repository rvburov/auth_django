from rest_framework import serializers

class OAuthCallbackSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    state = serializers.CharField(required=False)
    error = serializers.CharField(required=False)
    
    def validate(self, data):
        if data.get('error'):
            raise serializers.ValidationError(data['error'])
        return data
