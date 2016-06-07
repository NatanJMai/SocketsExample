## About

- Network course at Federal University of Fronteira Sul.
- Just an example of socket communication.  
- The server receives a file with products, quantity and values to calculate and return the sum of them.

### Requirements
crypto==1.4.1
pycrypto==2.6.1

sudo apt-get install python3-pip
pip3 install -r requirements.txt

### Running
First, we should create one file with products details. 
* *list_of_products* is a list of some products found at internet. 
* *file_destination* is the target file for we use after.

```sh
$ python3 create_products.py number_of_products list_of_products file_destination
```
```sh
$ python3 server.py host_ip port_number
```
```sh
$ python3 client.py file_products host_ip port_number
```

### Example
```sh
$ python3 create_products.py 10 products.txt file3.txt
```
```sh
$ python3 server.py localhost 50009
```
```sh
$ python3 client file3.txt localhost 50009
```

NatanJMai
