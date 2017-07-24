proxy_charles = 'PROXY <ipaddress>:8888;DIRECT;';

direct_hosts = [
  "s.mzstatic.com",
  "itunes.apple.com"
]

function FindProxyForURL(url, host) {

  if (direct_hosts.indexOf(host)!=-1) {
    return 'DIRECT;';
  }

  return proxy_charles;
}
