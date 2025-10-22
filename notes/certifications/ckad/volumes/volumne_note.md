---
title: "Volumne Note"
description: "Kubernetes PV and PVC cross-namespace access using StorageClass for dynamic provisioning"
tags: [kubernetes, volumes, ckad, storage, pv-pvc]
---
- PV can not be bounded to PVC in differnet namespace by default
  - To resolve that we can use storage-class.
  - The StorageClass is a cluster-wide resource that defines the provisioning parameters for different types of storage.
    This way, you could have PVCs in different namespaces using the same StorageClass, resulting in dynamically provisioned PVs.
