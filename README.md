# COMP90024_Assignment2

## Team Members

Xiaoyi Han 1130315  
Ka Hou Hong 1178062  
Ziyuan Xu 1124236  
Xiaoyue Lin 924655  
Xingyang Shen 928713  


## Video links
Cloud-based solution with dynamic deployment and crawler explanation:  
https://www.youtube.com/watch?v=Ut3a5CFF46E

Frontend and CouchDB Presentation:  
https://www.youtube.com/watch?v=xXDzmZHzU_Y

## Demo slide
https://docs.google.com/presentation/d/1gnVthEg6l9-BD5qJXGccGCIrEmOR3MMtdziJS-EXzd4/edit?usp=sharing

## System Architecture
![System Architecture](https://tva1.sinaimg.cn/large/008i3skNgy1gqvir3eoamj31720u0dtf.jpg)

## For deployment
    First, clone this git repository
    1. cd /OpenStack_Docker_Couchdb  
    2. sudo ./1-deploy-vm.sh  
       Enter the OpenStack Password  
    3. sudo ./2-deploy-setup.sh  
        Enter the OpenStack Password  
    4. sudo ./3-deploy-crawler.sh  
        Enter the OpenStack Password  

## For development
  ### Frontend
    cd frondend/ docker-compose up

  ### Backend
    cd backend/ docker-compose up

  ### Crawler
    cd crawler/ docker-compose up
## Instance Arrangement
    Instance1: 172.26.131.136
    Instance2: 172.26.132.130
    Instance3: 172.26.128.33
    Instance4: 172.26.133.27

