[![Package](https://github.com/nadzhou/ampdb/actions/workflows/package.yml/badge.svg)](https://github.com/nadzhou/ampdb/actions/workflows/package.yml)
# AMPdb - Database for structure-calculated AMPs 
Django framework for the protein AMPs database. With a clean and easy GUI, AMPdb provides an easy lookup for structural AMPs with its tabulated properties in each entry. 

## Introudction 
AbAMPdb is the manually-curated database for antimicrobial peptides (AMPs) specifically against Acinetobacter baumannii. The database provides predicted information related to antimicrobial potentials, homology-based modelled structures and the peptide protein interactions of these AMPs.

## interface
The AMPdb app looks as follows: 

### Home page


![image](https://github.com/nadzhou/ampdb/blob/main/static/img/interface1.png)

### Select AMP and protein tab


![image](https://github.com/nadzhou/ampdb/blob/main/static/img/interface2.png)

### Physicochemical parameter tab

![image](https://github.com/nadzhou/ampdb/blob/main/static/img/interface3.png)
### AMP-Target protein Interaction tab

![image](https://github.com/nadzhou/ampdb/blob/main/static/img/interface4.png)

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


