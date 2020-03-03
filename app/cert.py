import ssl
from urllib.parse import urlparse
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def isOrganization(url):
  """
  Function looks up the SSL certificate for the domain, and checks if 
  it is an OV or EV certificate by reading the following CertificatePolicies
  2.23.140.1.2.2: Organization Validation
  2.23.140.1.1: Extended Validation 
  """
  parsed_uri = urlparse(url)

  # Create a real connection in order to support SNI (server name indication)
  conn = ssl.create_connection((parsed_uri.netloc, 443))
  context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
  sock = context.wrap_socket(conn, server_hostname=parsed_uri.netloc)
  cert_pem = ssl.DER_cert_to_PEM_cert(sock.getpeercert(True))
  cert = x509.load_pem_x509_certificate(cert_pem.encode(), default_backend())
  
  # Find the certificate type
  for policy in cert.extensions.get_extension_for_class(x509.CertificatePolicies).value:
    oid = policy.policy_identifier.dotted_string
    if oid == '2.23.140.1.2.2' or oid == '2.23.140.1.1':
      return True

  return False
