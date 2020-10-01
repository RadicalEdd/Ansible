#!/usr/bin/python
import json
import re
import sys
# from ansible.parsing.ajson import AnsibleJSONEncoder


class FilterModule(object):
    def filters(self):
        return {
            # json
            'return_api': self.return_api,
            'return_json': self.return_json,
            'filter_server_names': self.filter_server_names,
            'filter_server_list': self.filter_server_list,
            'filter_port_numbers': self.filter_port_numbers,
            'filter_type_server': self.filter_type_server,
            'filter_mng_nodes': self.filter_mng_nodes,
            'filter_mng_nodes_name': self.filter_mng_nodes_name,
            'filter_mng_nodes_ip': self.filter_mng_nodes_ip,
            'filter_mng_nodes_port': self.filter_mng_nodes_port,
            'filter_env_code': self.filter_env_code,
            'filter_domain_name': self.filter_domain_name,
            'filter_country_name': self.filter_country_name,
            'filter_variables': self.filter_variables,
            'filter_hcp': self.filter_hcp,
        }

    # Return all data from api
    def return_api(self, content):
        json_dump = content
        print(json.dumps(json_dump))

    # Return json part from api
    def return_json(self, content):
        json_dump = content['json']
        print(json.dumps(json_dump))

    # Return list of all domain names
    def filter_server_names(self, content):
        for i in range(len(content['json'])):
            print(json.dumps(content['json'][i]['name']))

    # Return list of all server names
    def filter_server_list(self, content):
        for i in range(len(content['json'])):
            print(json.dumps(content['json'][i]['Servers'].keys()))

    # Return list of port numbers
    def filter_port_numbers(self, content):
        for i in range(len(content['json'])):
            for y in range(len(content['json'][i]['Servers'].values())):
                print(json.dumps(content['json'][i]['Servers'].values()[y]['ListenPortSSL']))

    # Return list of type of servers (mng/adm)
    def filter_type_server(self, content):
        for i in range(len(content['json'])):
            for y in range(len(content['json'][i]['Servers'].values())):
                print(json.dumps(content['json'][i]['Servers'].values()[y]['type']))

    # Filter managed nodes based on type and return 3 lists of Cluster_Name, IP and Listening address
    def filter_mng_nodes(self, content):
        name_list = []
        ip_list = []
        port_list = []

        for i in range(len(content['json'])):
            for y in range(len(content['json'][i]['Servers'].values())):
                if (content['json'][i]['Servers'].values()[y]['type']) == 'mng':
                    # Json dumps will create a string from each element
                    server_name = json.dumps(content['json'][i]['Servers'].values()[y]['Cluster']).strip('"')
                    server_listen_address = json.dumps(content['json'][i]['Servers'].values()[y]['ListenAddress']).strip('"')
                    server_listen_port = json.dumps(content['json'][i]['Servers'].values()[y]['ListenPort']).strip('"')

                    # Create 3 lists: Cluster_Name, IP, Port
                    name_list.append(server_name)
                    ip_list.append(server_listen_address)
                    port_list.append(server_listen_port)

        # Returning a list with string elements in it
        print(name_list)
        print(ip_list)
        print(port_list)

    # Filter managed nodes based on type and return a list with Cluster Name
    def filter_mng_nodes_name(self, content):
        server_list = []

        for i in range(len(content['json'])):
            for y in range(len(content['json'][i]['Servers'].values())):
                if (content['json'][i]['Servers'].values()[y]['type']) == 'mng':
                    server_name = json.dumps(content['json'][i]['Servers'].values()[y]['Cluster']).strip('"')
                    server_list.append(server_name)

        return server_list

    # Filter managed nodes based on type and return a list with IP
    def filter_mng_nodes_ip(self, content):
        ip_list = []

        for i in range(len(content['json'])):
            for y in range(len(content['json'][i]['Servers'].values())):
                if (content['json'][i]['Servers'].values()[y]['type']) == 'mng':
                    server_listen_address = json.dumps(content['json'][i]['Servers'].values()[y]['ListenAddress']).strip('"')
                    ip_list.append(server_listen_address)

        return ip_list

    # Filter managed nodes based on type and return a list with Port
    def filter_mng_nodes_port(self, content):
        port_list = []

        for i in range(len(content['json'])):
            for y in range(len(content['json'][i]['Servers'].values())):
                if (content['json'][i]['Servers'].values()[y]['type']) == 'mng':
                    server_listen_port = json.dumps(content['json'][i]['Servers'].values()[y]['ListenPort']).strip('"')
                    port_list.append(server_listen_port)

        return port_list

    # Filter env code eg. cn00a1
    def filter_env_code(self, content):
        env_code = (json.dumps(content['json']['code']).strip('"')).lower()
        return env_code

    # Filter domain name eg. cn.infra
    def filter_domain_name(self, content):
        domain_name = json.dumps(content['json']['domain']).strip('"')
        return domain_name

    # Filter domain name eg. cn/cz
    def filter_country_name(self, content):
        country_name = ((json.dumps(content['json']['domain']).strip('"')).split('.')[0]).upper()
        return country_name

    # To solve problems with multiple IP:Port in Weblogic cluster we will create lists inside dictionary
    # Create a lists inside dictionary
    def filter_variables(self, content):
        # application_dictionary = defaultdict(list)
        application_dictionary = {}

        for i in range(len(content['json'])):
            for y in range(len(content['json'][i]['Servers'].values())):
                if (content['json'][i]['Servers'].values()[y]['type']) == 'mng':
                    server_name = json.dumps(content['json'][i]['Servers'].values()[y]['Cluster']).strip('"')
                    server_listen_address = json.dumps(content['json'][i]['Servers'].values()[y]['ListenAddress'])\
                        .strip('"')
                    server_listen_port = json.dumps(content['json'][i]['Servers'].values()[y]['ListenPort']).strip('"')
                    ip_port = "{}:{}".format(server_listen_address, server_listen_port)

                    application_dictionary.setdefault(server_name, []).append(ip_port)

        return application_dictionary

    # Because of variable amount of hcp nodes we need to add filter which creates list of all hcp nodes
    def filter_hcp(self, content):
        hcp_list = []
        for k, v in (content['json'].items()):
            if re.match(r"hcp0[02-9]", k):
                hcp_list.append(k)
        return hcp_list

        # for i in range(len(content['json'].keys())):
        #     print(json.dumps(content['json'].keys()))

