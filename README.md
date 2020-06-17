# Generate JWT tokens for use with server-to-server Google applications

This is a convience tool that generates JWT tokens to access applications on Google's infrastructure. Mainly useful if you are accessing the application from outside of the GCP boundary. Once the token is generated you can access applications hosted in Google cloud platform with a `Authorization` header set to `Bearer <token>`.

The executable ZIP module is self-contained and holds all the dependencies it needs. Compatible with Python 2.7 and 3.x

## Build

If all you want is a pre-built binary, check out the releases page.

* Requires pip installed with Python 2.7 (purely to support Python 2)
* Run `./package.sh` to generate the executable

## Usage

```
usage: gen-id-token.pyz [-h] --audience AUDIENCE --key-file KEY_FILE

optional arguments:
  -h, --help           show this help message and exit
  --audience AUDIENCE  Audience
  --key-file KEY_FILE  Service Account Key
```
