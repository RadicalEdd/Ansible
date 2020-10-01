# confluent_platform_configuration


<h1> Optional password: </h1>

Its possible to set up optional password for Kafka (default is "Pass0rd"): 

```json
 "vars": {
              "mw_repo_server": "$LC{datacenter.repo_host}",
              **"prod_password": "This_will_be_option password"**
              "mw_java_user": "root",
              "mw_java_group": "root",
              "mw_java_puppet_role": "role_adoptopenjdk_8u222_puppet",
              "embedit_team_type": "CD01 MIDDLEWARE"
            }
```           

<h1> Template example: </h1>

```json
"confluent_platform_configuration": {
        "Inventory": {
          "mw_confluent_platform_conf_hosts": {
            "children": {
              "zookeeper": {
                "hosts": {
                  "cpzoo01-$LC{env.code}.$LC{env.domain}": {},
                  "cpzoo02-$LC{env.code}.$LC{env.domain}": {},
                  "cpzoo03-$LC{env.code}.$LC{env.domain}": {}
                }
              },
              "broker": {
                "hosts": {
                  "cpkafka01-$LC{env.code}.$LC{env.domain}": {},
                  "cpkafka02-$LC{env.code}.$LC{env.domain}": {},
                  "cpkafka03-$LC{env.code}.$LC{env.domain}": {}
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
              "mw_java_user": "root",
              "mw_java_group": "root",
              "mw_java_puppet_role": "role_adoptopenjdk_8u222_puppet",
              "embedit_team_type": "CD01 MIDDLEWARE"
            }
          }
        },
        "AnsiblePlays": {
          "inventory_play": null,
          "verbose": 2,
          "provisioning_play": "confluent_platform_configuration.yml",
          "repo": "mw_confluent_platform",
          "path": "git@git.homecredit.net:ansible/playbooks/infra_mw",
          "gitref": "master"
        }
      }
```
