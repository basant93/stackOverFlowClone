from .models import UserProfile
from django.shortcuts import get_object_or_404

def add_variable_to_context(request):

    reputation_count = get_object_or_404(UserProfile, user_id=1)

    return {
        'testme': reputation_count.reputation
    }