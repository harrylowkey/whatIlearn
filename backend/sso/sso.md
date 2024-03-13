# SSO

1. Service proivders
- Gmail
- Youtube

2. Identity providers
- Auth0
- Keycloak


## Flow


Single Sign-On (SSO) is a mechanism that allows users to authenticate once and gain access to multiple related, but independent, software systems without being prompted to log in again at each of them. Here's a generalized flow of how SSO typically works:

1. User Access Request: The user attempts to access a protected resource or application within the system that requires authentication.
2. Check for Authentication Token: If the user does not have an active session (authentication token), they are redirected to the SSO server for authentication.
3. Authentication Request: The user is presented with a login screen where they enter their credentials (e.g., username and password).
4. Authentication Verification: The SSO server validates the user's credentials against the user database. This can involve various authentication methods such as LDAP, Active Directory, OAuth, OpenID Connect, SAML, etc.
5. Issuance of Authentication Token: If the credentials are valid, the SSO server creates a secure authentication token or session identifier and associates it with the user's session.
6. Redirect Back to Application: The SSO server redirects the user back to the original application or resource they were trying to access, passing along the authentication token in the request.
7. Resource Access: The application receives the authentication token and validates it with the SSO server.
8. Access Verification: The application verifies the authentication token with the SSO server to ensure its validity and authenticity.
9. User Access Granted: If the authentication token is valid, the user is granted access to the application or resource without having to re-enter their credentials.
10. Session Management: The SSO server manages the user's session, handling tasks such as session timeouts, logout, and session invalidation.
11. Access to Additional Resources: If the user tries to access another application or resource within the same SSO ecosystem, they can do so seamlessly without needing to log in again, as long as their session is active.
12. Logout: When the user chooses to log out, the SSO server invalidates the session token, effectively logging the user out of all associated applications and resources.
