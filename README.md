# k8s-backup-dump

# Purpose

Split out aggregated cluster YAML dumps to individual files.

Items will be organized into the format `<namespace>/<name>/<kind>.yaml` and written out into a tree beneath the current working path.

# Notes

This is beta software and may not be fit for your own use.

YAML is filtered within the dumpItem routine to remove cluster specific elements (such as object uid, selfLink, etc.)

# Usage

```
kubectl get all --all-namespaces -o yaml > cluster.yaml
kubectl get ingress --all-namespaces -o yaml > ingress.yaml
kubectl get secrets --all-namespaces -o yaml > secrets.yaml
./k8s-backup-dump.py cluster.yaml ingress.yaml secrets.yaml
```
