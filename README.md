# k8s-backup-dump

# Purpose

Split out aggregated cluster YAML dumps to individual files.

Items will be organized into the format `<namespace>/<name>/<kind>.yaml` and written out into a tree beneath the current working path.

The `kubectl get all` command does not return all objects. (See https://github.com/kubernetes/kubectl/issues/151) It is not functionally complete to backup all objects in a cluster.

It is recommended to track YAML being applied to a cluster in source control. Sometimes it is desirable to not track certain types of objects in source control (for instance secrets.) There may be times where it is necessary to have a backup (such as during major version upgrades, cluster maintenance, etc.)

When performing a backup, please ensure the resulting backup or backups contains objects that are critical for your restore.

The script is meant to extract objects from a YAML list for the purpose of performing a targetted restore of specific objects. Additionally the script is not intended to extract all objects for the purpose of a blanket restore.

# Notes

This is beta software and may not be fit for your own use.

YAML is filtered within the `dumpItem` function to remove cluster specific elements (such as item's `metadata.uid`, `metadata.selfLink`, some `metadata.annotations`, `status`, etc.)

# Usage

```
kubectl get all --all-namespaces -o yaml > cluster.yaml
kubectl get configmaps --all-namespaces -o yaml > configmaps.yaml
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
