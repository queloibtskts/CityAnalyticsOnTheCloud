# City Analytics On The Cloud
A Cluster and Cloud Computing project focusing on using the UniMelb Research Cloud and Twitter data to tell interesting stories of life in Australian cities.\
We are interested in (studying) swearing. 🙊

- Carried out a variety of social media data analytics scenarios related to profanity 
- Developed a Cloud-based solution that exploited a multitude of virtual machines across the Melbourne Research Cloud (MRC) for mining and storing 10 thousand+ tweets 
- Built a Twitter harvester using Python3 and Twitter APIs
- Developed analytic scenarios using the MapReduce capabilities offered by CouchDB for social media analytics, and visualising data using React, Material-UI and Tableau JavaScript API on the front-end.
- Deployed the application (including CouchDB, the harvester and the front-end web application) to MRC servers using Ansible, Docker
- See project poster: https://www.canva.com/design/DAEmVFPZFmc/nQjew5bQIDJLhOkSOoOSZg/view?utm_content=DAEmVFPZFmc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Team Members
We are a group of Master students from the University of Melbourne.

- Xiaoyi Han
- Ka Hou Hong https://www.linkedin.com/in/ka-hou-hong-47462a14a/
- Ziyuan Xu https://www.linkedin.com/in/lengary/
- Xiaoyue Lin https://www.linkedin.com/in/xiaoyue-lin-chloe/
- Xingyang Shen

## System Architecture
![System Architecture](https://tva1.sinaimg.cn/large/008i3skNgy1gqvir3eoamj31720u0dtf.jpg)

## Demo Video links
Cloud-based solution with dynamic deployment and crawler explanation:  
https://www.youtube.com/watch?v=Ut3a5CFF46E

CouchDB and Frontend analytics presentation:  
https://www.youtube.com/watch?v=xXDzmZHzU_Y

## Demo slide
https://docs.google.com/presentation/d/1gnVthEg6l9-BD5qJXGccGCIrEmOR3MMtdziJS-EXzd4/edit?usp=sharing

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

