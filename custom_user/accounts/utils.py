import os
import uuid


# Gender choices
GEN_CHOICE = (
    ('M', 'Male'),
    ('F', 'Female')
)


# profile image location
def _Profile_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('profile_pictures/', filename)

