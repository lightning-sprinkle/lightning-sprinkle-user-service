import dns.resolver

def get_lnd_pubkey(hostname):
  """
  Get the lnd pubkey from a hostname by querying the DNS records for a TXT entry.
  """
  print(hostname)
  answers = dns.resolver.query(hostname, "TXT")
  for rdata in answers:
    record = rdata.to_text()
    print(record[:12])
    if record[:12] == '"lnd-pubkey=':
      return record[12:12+66]