
MAJOR = 0
MINOR = 0
PATCH = 1

version_info = (MAJOR, MINOR, PATCH)
version = '%i.%i.%i' % version_info
__version__ = version

__all__ = ['version', 'version_info', '__version__']
