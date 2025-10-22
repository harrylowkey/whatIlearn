---
title: "Migrate keycloak database"
description: "Step-by-step process for migrating Keycloak database including realm export, pg_dump, and data standardization"
tags:
  - database
  - keycloak
  - migration
  - postgresql
  - pg_dump
---
1. Export realm settings
2. Empty the policies property ([Issue](https://github.com/keycloak/keycloak/issues/11664#issuecomment-1111062102))
3. Import realm settings
4. pg_dump the original keycloak database
5. psql restore the original keycloak database
6. standardize user_entity, user_role_mapping, credential if needed
