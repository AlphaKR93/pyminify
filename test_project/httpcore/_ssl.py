import ssl,certifi
def default_ssl_context():context=ssl.create_default_context();context.load_verify_locations(certifi.where());return context