What is SSL/TLS termination?
SSL termination is when the load balancer is terminating the SSL connection. That is, it is the end of the SSL connection and the onward connection to the back-end is conducted via unencrypted means.

What is SSL/TLS offload?
SSL offload is when the burden of SSL related functions pertaining to the connection is offloaded to the load balancer. This relieves the cryptographic strain from the real servers.

OK, that makes it simpler, right? Good. Now that we understand that, it's probably worth pointing out that SSL termination is a specific function of SSL offload. That means that all SSL termination is SSL offload but not all SSL offload is SSL termination.
