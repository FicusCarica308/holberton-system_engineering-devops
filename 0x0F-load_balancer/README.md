PRJ: 0x0F-load_balancer\
DES: This project contains a few bash scripts setting up a haproxy load balancer for two addition servers\
TASKS:\
0-custom_http_response_header  - configures nginx with a new custom header X-Served-By with the servers hostname as its value\
1-install_load_balancer - Install haproxy on the servers its run on, then configures it with a backend/frontend and init script capabilities\
2-puppet_custom_http_response_header.pp - Task 0 but with puppet manifest automation\
DATE: 4 - 12 - 2021\
NAME: MANUEL FIGUEROA
