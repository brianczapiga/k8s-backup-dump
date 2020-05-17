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

# License

```
k8s-backup-dump for splitting out k8s cluster YAML lists into separate files
Copyright (C) 2020    Brian Czapiga

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

See <http://www.gnu.org/licenses/> for more information.
```
