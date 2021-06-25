# 存储

## PersistentVolume

### hostpath

> A hostPath volume mounts a file or directory from the host node's filesystem into your Pod. This is not something that most Pods will need, but it offers a powerful escape hatch(逃生舱，比喻平时不怎么用，但又有相当实用价值的东西) for some applications.

> For example, some uses for a hostPath are:
> - running a container that needs access to Docker internals; use a hostPath of /var/lib/docker
> - running cAdvisor in a container; use a hostPath of /sys
> - allowing a Pod to specify whether a given hostPath should exist prior to the Pod running, whether it should be created, and what it should exist as

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: k8s.gcr.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /test-pd
      name: test-volume
  volumes:
  - name: test-volume
    hostPath:
      # directory location on host
      path: /data
```

### local

> You must set a PersistentVolume nodeAffinity when using local volumes. The Kubernetes scheduler uses the PersistentVolume nodeAffinity to schedule these Pods to the correct node.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: netdata-data
spec:
  capacity:
    storage: 10Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  local:
    path: /data/netdata-data
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        # 对应节点标签 type=node
        - key: yym.com/netdata
          operator: Exists
```

## 参考

1. https://kubernetes.io/docs/concepts/storage/volumes/#local
