# AMPdb - Database for structure-calculated AMPs 
Django framework for the protein AMPs database. With a clean and easy GUI, AMPdb provides an easy lookup for structural AMPs with its tabulated properties in each entry. 

## Introudction 
AbAMPdb is the manually-curated database for antimicrobial peptides (AMPs) specifically against Acinetobacter baumannii. The database provides predicted information related to antimicrobial potentials, homology-based modelled structures and the peptide protein interactions of these AMPs.

## interface
The AMPdb app looks as follows: 

### Home page


![image](https://user-images.githubusercontent.com/25282805/130806245-0cdac0a2-be04-4d7e-9671-7edd1d3976c3.png)

### Results page


![image](https://user-images.githubusercontent.com/25282805/130806466-baf02c4b-efd5-45d8-95db-8569e563da51.png)

### Docking tab

![image](https://user-images.githubusercontent.com/25282805/130806645-0a79effd-b446-4211-afef-672718c7b146.png)

## Installation 
Installation is easy, just follow these steps: 
```
    $ git clone https://github.com/nadzhou/ampdb.git
    $ cd ampdb 
    $ 
    $ conda env import environment.yml 
```
Activate the Conda environment by 
```
    $ conda activate db
```

Then to access the database, just run the following command>: 
````
  $ python manage.py runserver
````

## Motivation 


## Goals 

