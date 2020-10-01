HTTP conf generator
-------------------
  
  Generate and upload httpd.conf for apache proxy

Preparation
-----------

  NOTE: Ansible 2.7 with python 2.7 is required ! 

  git clone
  
  git branch -a your_branch

  edit group_vars/all.yml    # update path where's your own administ cert. location
  
  
Run playbook (examples)
-----------------------
  
  - generate and upload httpd conf for whole cn00c1

  ansible-playbook main.yml --extra-vars env=cn00c1 -v    

   
  - just generate httpd conf for whole cn00c1

  ansible-playbook main.yml --extra-vars env=cn00c1 --tags generate_http_conf -v    
   
  
  - just upload httpd conf for whole cn00c1

  ansible-playbook main.yml --extra-vars env=cn00c1 --tags upload_http_conf -v    


List of tags
------------

  play #1 (dns): Fix dns cn.infra       TAGS: [nsupdate_all]
  TASK TAGS: [nsupdate_all, nsupdate_cn, nsupdate_cz, nsupdate_perf]

  play #2 (all): Generate httpd conf    TAGS: [generate_http_conf]
  TASK TAGS: [generate_http_conf]

  play #3 (all): Upload httpd conf      TAGS: [upload_http_conf] 
  TASK TAGS: [upload_http_conf]
