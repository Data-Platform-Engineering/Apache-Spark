# This repo generates data to be used for spark processing.

## Setup
### **1. Prerequisites**
- Python 3.9.13, Spark & JVM
- Access to AWS with permissions to provision an s3 bucket, EMR, and EC2 services. 

### **2. Infrastructure Setup**
- TO DO ?

### **3. Virtual Env setup**
- Set up your virtual env by installing all packages in the `requirements.txt` file 

`
pip install -r requirements.txt
`

### **4. Project run - Local**
- The main project is in the `hellospark.py` file. Edit it to the number of records you want and run the command below

`
python hellospark.py
`

### **5. Running it on your cluster**
- To submit this project on your cluster, clone the repo, cd into the directory and run the command below:

`
spark-submit
--master yarn
--deploy-mode cluster
--num-executors 4
--executor-memory 4G
--executor-cores 2
hellospark.py
`
