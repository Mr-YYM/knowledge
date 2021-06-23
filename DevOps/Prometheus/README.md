## Prometheus 的服务发现能力

- 实现机制

  - 云原生时代下，计算资源可以根据需求进行弹性伸缩。这意味着我们的监控系统的监控目标是动态变化的，传统的 Push 模式的监控软件已经无法满足新需求。而对于 Prometheus 这一类基于 Pull 模式的监控系统，显然也无法继续使用的 static_configs 的方式静态的定义监控目标。
  - 对于 Prometheus 而言其解决方案就是引入一个**中间的代理人（服务注册中心）**
  - 这个代理人掌握着当前所有监控目标的访问信息，Prometheus 只需要向这个代理人询问有哪些监控目标即可
  - 这种模式被称为**服务发现**。
  - 在 Kubernetes 这类容器管理平台中，Kubernetes掌握并管理着所有的容器以及服务信息，那此时 Prometheus 只需要与 Kubernetes 打交道就可以找到所有需要监控的容器以及服务对象。

## HELM 部署

- 部署

  ```shell
  helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
  # 查看 kube-prometheus-stack 版本号
  helm search repo prometheus-community/kube-prometheus-stack -l | head
  # 下载并解压 chart
  helm pull prometheus-community/kube-prometheus-stack --untar --version 11.1.0

  # 使用自定义的 cutome-values.yaml 进行部署（helm3）
  kubectl create ns monitoring
  helm upgrade --install \
    --namespace monitoring \
    -f custom-values.yaml \
    kube-prometheus-stack \
    ./kube-prometheus-stack
  ```

## 参考

1. https://github.com/ryan4yin/DevOps/tree/master/telemetry/metrics%20-%20prometheus%2Bgrafana/kube-prometheus
