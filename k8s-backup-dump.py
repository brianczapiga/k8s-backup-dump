#!/usr/local/bin/python3
# k8s-backup-dump by Brian Joseph Czapiga <brian@czapiga.com>

# Usage:
#   kubectl get all --all-namespaces -o yaml > cluster.yaml
#   kubectl get configmaps --all-namespaces -o yaml > configmaps.yaml
#   kubectl get ingress --all-namespaces -o yaml > ingress.yaml
#   kubectl get secrets --all-namespaces -o yaml > secrets.yaml

#   ./k8s-backup-dump.py cluster.yaml configmaps.yaml ingress.yaml secrets.yaml

# The following types are handled by the script but were not a primary design consideration:

#   kubectl get clusterrole --all-namespaces -o yaml > clusterroles.yaml
#   kubectl get clusterrolebinding --all-namespaces -o yaml > clusterrolebindings.yaml
#   kubectl get role --all-namespaces -o yaml > roles.yaml
#   kubectl get rolebinding --all-namespaces -o yaml > rolebindings.yaml
#   kubectl get serviceaccount --all-namespaces -o yaml > serviceaccounts.yaml

#   ./k8s-backup-dump.py clusterroles.yaml clusterrolebindings.yaml roles.yaml rolebindings.yaml serviceaccounts.yaml

import yaml
import sys
import os

version = '0.0.1'
debug = False

writeKinds = [
  'ConfigMap',
  'ClusterRole',
  'ClusterRoleBinding',
  'DaemonSet',
  'Deployment',
  'HorizontalPodAutoscaler',
  'Role',
  'RoleBinding',
  'Secret',
  'Service',
  'ServiceAccount',
  'StatefulSet',
  'Ingress'
]

ignoreKinds = [
  'Pod',
  'ReplicaSet',
  'Job'
]

def usage():
  print("Usage: " + sys.argv[0] + " [ dump.yaml ]\n")

def dumpItem(item):
  if 'kind' not in item:
    print("WARN: List item does not have a \'kind\'.")
    if debug:
      print(yaml.dump(item)) 
      sys.exit(1)
    return None

  if item['kind'] not in writeKinds:
    if item['kind'] not in ignoreKinds:
      print("WARN: List item kind is \'" + item['kind'] + "\'.")
    return None

  if 'metadata' not in item:
    print("WARN: List item does not have metadata.")
    if debug:
      print(yaml.dump(item)) 
      sys.exit(1)
    return None

  # Filters
  removeMetadata = ['selfLink', 'uid', 'creationTimestamp', 'generation', 'resourceVersion']
  for metaElement in removeMetadata:
    if metaElement in item['metadata']:
      del item['metadata'][metaElement]

  if 'annotations' in item['metadata']:
    if 'kubectl.kubernetes.io/last-applied-configuration' in item['metadata']['annotations']:
      del item['metadata']['annotations']['kubectl.kubernetes.io/last-applied-configuration']

  if 'status' in item:
    del item['status']

  basename = ''
  if 'namespace' in item['metadata']:
    namespace = item['metadata']['namespace']
    basename = namespace + '/'
  basename = basename + item['metadata']['name']
  kind = item['kind'].lower()

  
  if not os.path.exists(basename):
    splitpath = basename.split('/')
    for a in range(len(splitpath)):
      dir = os.sep.join(splitpath[0:(a+1)])
      if not os.path.exists(dir):
        print("INFO: mkdir: " + dir)
        os.mkdir(dir)

  filename = basename + '/' + kind + '.yaml'
  print("INFO: write: " + filename)
  with open(filename,'w+') as file:
    file.write(yaml.dump(item))
    file.close()

  return True

def main():
  if len(sys.argv) <= 1:
    usage()
    sys.exit(1)

  yaml_files = sys.argv[1:]

  for yaml_file in yaml_files:
    cluster = {}

    with open(yaml_file) as file:
      cluster = yaml.load(file, Loader=yaml.FullLoader)

    if cluster['kind'] == 'List':
      for item in cluster['items']:
        dumpItem(item)

if __name__ == '__main__':
  main()
