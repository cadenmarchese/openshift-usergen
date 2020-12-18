This is a Python3 script that reads a desired username and password, writes a htpasswd file, and then applies the htpasswd file to the cluster as a cluster-wide oauth custom resource: 

```
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: htpasswd
    mappingMethod: claim
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpasswd-secret
```

It also prompts whether or not to assign cluster-admin privileges, or else will leave the user permissions alone for the administrator to decide what cluster role to apply later.

This will work on Linux and macOS clients with htpasswd and the OC CLI installed, and will not remove the kubeadmin user. This will not work if you alrady have a custom resource for authentication in place, and will not log into your cluster for you.

