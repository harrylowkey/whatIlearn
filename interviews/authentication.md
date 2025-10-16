---
title: "Authentication Methods"
---
# Users to Services

## 1. Basic Authentication (username/password)
- **How it works:** Send base64-encoded username and password in the Authorization header.  
- **Use case:** Simple APIs or legacy systems.  
- **Pros:** Easy to implement.  
- **Cons:** Credentials sent each request, must always use HTTPS, not scalable for multi-service environments.

## 2. OAuth2 Authorization Code / JWT Flow (for external users)
- **How it works:** External users log in, get an access token via OAuth2 flows; API verifies the token.  
- **Use case:** End-user authentication for third-party apps or web clients.  
- **Pros:** Standardized, supports user delegation, refresh tokens.  
- **Cons:** Overkill for internal service-to-service authentication.

# Services to Services

## 1. OAuth2 with Client Credentials
- **How it works:** Client provides `client_id` and `client_secret` to an authorization server, receives a JWT or opaque access token.  
- **Use case:** External services, third-party clients, or when you need standardization and token revocation.  
- **Token type:** JWT (HMAC/RSA) or opaque token.  
- **Pros:** Standardized, supports scopes, revocation, and multi-client.  
- **Cons:** Slightly complex to implement, requires an auth server.

## 2. Signed Service Token (SST)
- **How it works:** Services you control generate tokens themselves using a shared secret (HMAC) or private key (RSA). The other service verifies signature and claims.  
- **Use case:** Internal services you fully control.  
- **Token type:** JWT or custom signed token.  
- **Pros:** Lightweight, avoids token issuance round-trips, fast.  
- **Cons:** Not suitable for untrusted clients, requires secret/key management.

## 3. Hardcoded API Key
- **How it works:** Services share a static API key stored in code or config; each request includes the key in headers.  
- **Use case:** Simple internal service-to-service calls or legacy systems.  
- **Pros:** Extremely simple, no token management.  
- **Cons:** No expiry, easy to leak, hard to rotate, not scalable.

## 4. HMAC-Signed Request (per-request signature)
- **How it works:** Client signs **each request** with a secret key and timestamp; server verifies signature.  
- **Pros:** Protects against replay attacks and tampering.  
- **Cons:** Requires client to generate per-request signature, more complex than static tokens.
- **Use case:** APIs where replay protection is needed (e.g., AWS API request signing, webhook signing).  

#### AWS API Request Signing (Signature Version 4)

**How it works:**
- Every request to AWS services (S3, DynamoDB, etc.) is signed with the client’s secret key using HMAC-SHA256.
- The signature includes the request method, URL, headers, and timestamp.
- AWS verifies the signature on every request.

**Why:**
- Ensures requests are authentic and haven’t been tampered with.
- Prevents replay attacks because the signature is tied to a timestamp.

#### 2️⃣ Stripe Webhook Verification

**How it works:**
- Stripe signs each webhook payload using a secret key (HMAC-SHA256).
- Your server verifies the signature before processing the webhook.

**Why:**
- Ensures the webhook actually came from Stripe and wasn’t forged.
- Protects against replay or tampering.

#### 3️⃣ Internal Microservices with High-Security Requirements

**Scenario:** Payment or banking services between microservices.

**How it works:**
- Service A signs each request with HMAC using a shared secret.
- Service B verifies the signature and timestamp before processing.

**Why:**
- Prevents malicious replay of requests (e.g., duplicate transactions).
- Adds request integrity and authentication without issuing JWTs.


## 5. JWT Signed by a Central Auth Server (Microservices + Gateway)

- **How it works:** 
  - Central Auth Service issues JWTs for clients (external or internal).  
  - Requests from clients go through a **Gateway Service**.  
  - Gateway can either:  
    1. Verify the JWT locally using the public key.  
    2. Call the Auth Service to verify the token (token introspection).  

- **Use case:** 
  - Microservices architecture with external clients.  
  - Centralized authentication with a Gateway handling all client authentication.  

- **Pros:** 
  - Centralized authentication and token issuance.  
  - Gateway offloads auth logic from downstream services.  
  - Supports expiry, claims, scopes, and role-based access control.

- **Cons:** 
  - Gateway becomes a critical auth point (single point of failure if not redundant).  
  - Slight overhead if the Gateway generates internal tokens.


## 6. Mutual TLS (mTLS)
- **How it works:** Both client and server authenticate each other using X.509 certificates over TLS.  
- **Use case:** Highly secure internal/external service communication.  
- **Pros:** No token management needed, very strong authentication.  
- **Cons:** Certificate management is complex, setup overhead is higher.




