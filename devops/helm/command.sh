# Build dependency
helm dependency build .
helm upgrade *chart-name* . --namespace *namespace* --create-namespace --install
--create-namespace if not have namespace
--install if not have chart otherwise upgrade
