# prometheus
prometheus技术交流

1.Prometheus安装
git clone https://github.com/2777484478/prometheus.git
采用daemonset方式部署node-exporter组件
kubectl create -f  node-exporter.yaml 
部署prometheus组件
rbac文件
kubectl create -f  k8s-prometheus-grafana/prometheus/rbac-setup.yaml
以configmap的形式管理prometheus组件的配置文件
kubectl create -f  k8s-prometheus-grafana/prometheus/configmap.yaml 
Prometheus deployment 文件
kubectl create -f  k8s-prometheus-grafana/prometheus/prometheus.deploy.yml 
Prometheus service文件
kubectl create -f  k8s-prometheus-grafana/prometheus/prometheus.svc.yml 
部署grafana组件
grafana deployment配置文件
kubectl create -f   k8s-prometheus-grafana/grafana/grafana-deploy.yaml
grafana service配置文件
kubectl create -f   k8s-prometheus-grafana/grafana/grafana-svc.yaml
grafana ingress配置文件
kubectl create -f   k8s-prometheus-grafana/grafana/grafana-ing.yaml
