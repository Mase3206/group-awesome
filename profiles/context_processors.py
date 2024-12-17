from .models import SpaceTravelerProfile

def user_profile(request):
    """
    Make sure the user's profile is available everywhere.

    Returns
    -------
        additional context (dict[str, SpaceTravelerProfile | None]) : The currently signed-in user's profile, if it exists.

    Conditions
    ----------
    * If the user is not signed in, return None.
    * If the user is signed in but *has not* created their profile, return None.
    * If the user is signed in and *has* created their profile, return their profile object.
    """
    
    profile = None

    if request.user.is_authenticated:
        try:
            profile = SpaceTravelerProfile.objects.get(real_account=request.user)
        except SpaceTravelerProfile.DoesNotExist:
            pass
    
    return {'profile': profile}

