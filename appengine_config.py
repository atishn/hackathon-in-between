from google.appengine.ext import vendor


# Import 3rd party python libraries, necessary for google client api
# see: https://cloud.google.com/appengine/docs/python/tools/libraries27#vendoring
vendor.add('libs')


def namespace_manager_default_namespace_for_request():
    """
    used for setting the global namespace for all queries against the datastore
    :return: string to use for namespace
    """
    return 'v1'
