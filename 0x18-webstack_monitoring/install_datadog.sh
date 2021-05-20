#!/usr/bin/env bash
# installs datadog client on webserver
DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=f5579e2196cc3785cd0f495ed2a588f1 DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"
