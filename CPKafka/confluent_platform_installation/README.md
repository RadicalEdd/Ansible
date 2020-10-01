# confluent_platform_installation

Sample configuration:

For variables that can be overwritten check defaults/main.yml.

<h1> Template example: </h1>

```json
      "confluent_platform_installation": {
        "Inventory": {
          "mw_confluent_platform_install_hosts": {
            "hosts": {
              "cpkafka01-$LC{env.code}.$LC{env.domain}": {},
              "cpkafka02-$LC{env.code}.$LC{env.domain}": {},
              "cpkafka03-$LC{env.code}.$LC{env.domain}": {},
              "cpzoo01-$LC{env.code}.$LC{env.domain}": {},
              "cpzoo02-$LC{env.code}.$LC{env.domain}": {},
              "cpzoo03-$LC{env.code}.$LC{env.domain}": {},
              "cpkafkatools01-$LC{env.code}.$LC{env.domain}": {},
              "cpkafkatools02-$LC{env.code}.$LC{env.domain}": {}
            },
            "children": {
              "broker": {
                "hosts": {
                  "cpkafka01-$LC{env.code}.$LC{env.domain}": {},
                  "cpkafka02-$LC{env.code}.$LC{env.domain}": {},
                  "cpkafka03-$LC{env.code}.$LC{env.domain}": {}
                }
              },
              "zookeeper": {
                "hosts": {
                  "cpzoo01-$LC{env.code}.$LC{env.domain}": {},
                  "cpzoo02-$LC{env.code}.$LC{env.domain}": {},
                  "cpzoo03-$LC{env.code}.$LC{env.domain}": {}
                }
              },
              "schema-registry": {
                "hosts": {
                  "cpkafkatools01-$LC{env.code}.$LC{env.domain}": {},
                  "cpkafkatools02-$LC{env.code}.$LC{env.domain}": {}
                }
              }
            },
            "vars": {
              "mw_repo_server": "$LC{datacenter.repo_host}",
              "embedit_team_type": "CD01 MIDDLEWARE"
            }
          }
        },
        "AnsiblePlays": {
          "inventory_play": null,
          "verbose": 2,
          "provisioning_play": "confluent_platform_installation.yml",
          "repo": "mw_confluent_platform",
          "path": "git@git.homecredit.net:ansible/playbooks/infra_mw",
          "gitref": "master"
        }
      }
```
