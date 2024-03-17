1. Use opensource chart
# Add repo
helm repo add <repo-name> <url>   # Add a repository from the internet:

# Install chart from repo that installed before
helm install <name> <chart> # Install the chart with a name

# Upgrade or create new one 
helm upgrade <release> <chart> # Upgrade a release
helm upgrade <release-name> . --namespace <namespace> --create-namespace --install
--create-namespace if not have namespace
--install if not have chart otherwise upgrade


2. Build out chart from scratch
# Create chart direcroty with template files
helm create <name> # Creates a chart directory along with the common files and directories used in a chart.

# Build dependency
helm dependency build .
