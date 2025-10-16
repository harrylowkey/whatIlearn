---
title: "Cryptography"
---
1. Hash
-> md5, sha1, sha256, sha512

2. Salt

3. HMAC

4. Symmetric Encryption
- AES: Advanced Encryption Standard

5. Asymmetric Encryption
- RSA: Rivest-Shamir-Adleman
- public key, private key
- public key is used to encrypt, private key is used to decrypt
- public key is generated from private key
- not use to encrypt large data

- RSA + AES
- Chat 
- SSL
- SSH

6. Signing
-> use asymmetric encryption
- SSH

## Compare HMAC vs Digital Signing

When to Use Each
Use HMAC when:

You have a secure way to share keys between trusted parties
Performance is critical
You don't need to prove authenticity to third parties
Example: API authentication between your own services

Use Digital Signatures when:
You need non-repudiation (legal documents, contracts)
Multiple parties need to verify authenticity
You're dealing with untrusted parties
Example: Software distribution, blockchain transactions, email signing

Both ensure that data hasn't been tampered with, but digital signatures add the crucial ability to prove who created the message.
