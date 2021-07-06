# Istio

## Sidecar 注入原理

istio 他在 pod 里面注入了 envoy sidecar，deployment container 声明那儿没有指明入口的 port，暴露的 port 依然是业务容器的 port 。但是流量就被 sidecar 接管了，这是因为修改了 iptable 规则，直接把原本端口的流量强行流向 envoy

## 参考

1. https://jimmysong.io/istio-handbook/concepts/sidecar-injection-deep-dive.html
