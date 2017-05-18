#!/bin/bash

# Generate an SSL certificate file to serve content over https (one-time)
openssl req -new -x509 -keyout my-ssl-cert.pem -out my-ssl-cert.pem -days 365 -nodes
