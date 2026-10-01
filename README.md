# base64

A small Python script that builds an HTTP Basic authentication header from a username and password, then decodes it again to confirm the result.

## What it does

1. Prompts for a username (for example `DOMAIN\username`) and a password.
2. Joins them as `username:password`.
3. Base64-encodes the result and prints it as a `Basic ...` authentication header.
4. Decodes the Base64 value and prints it, so you can verify the round trip.

## Usage

```
python main.py
```

Example session (placeholder values):

```
Username (e.g. DOMAIN\username): DOMAIN\username
Password: example-password
plain_text = DOMAIN\username:example-password
Basic authentication = Basic RE9NQUlOXHVzZXJuYW1lOmV4YW1wbGUtcGFzc3dvcmQ=
decoded_text = b'DOMAIN\\username:example-password'
```

Requires Python 3 and only uses the standard library.

## Credential handling

- Credentials are entered at runtime and are not hardcoded in the source.
- Credentials are not stored to disk by this program.
- Credentials may exist in your terminal's scrollback output, because the script echoes the input, the encoded header and the decoded text.

## License

Licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for the full text.
