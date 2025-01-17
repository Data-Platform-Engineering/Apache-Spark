### PROJECT CONTEXT
To be able to effectively and efficiently digest Spark Learning, it's important to get some production like task to practice and see.
We are going to use the popular `Olist DataSet` which can be found [HERE](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?resource=download).
The end goal is to leverage Spark to process the `customer` and `geolocation` dataset, In addition to that, we will answer some business questions
from the dataset.
The project will have 2 sections, the `Infrastructure setup` and the `Data Processing`.

### Infrastructure requirements
The below are required and `Terraform` should be the standard means to deploy the infrastructures
- Dedicated VPC Stacks ( Don't use the Default VPC stacks )
- Production Grade `EMR Cluster` ( Spark ) deployment with Terraform
- Data Lake set up to hold the Olist `Customer` and `Geolocation` Dataset and also to write the result of each business questions.

### Data Processing
In the event of processing the Files with spark, some below Data processing requirement is required
- tbd
- tbd
- tbd
- tbd


### NOTE
The project expect a custom configuration for your spark application which should include 
- Number of Executors definition
- Number of Cores and Memory allocated to each Executor definition 
  
