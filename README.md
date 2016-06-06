## About

- Network course at Federal University of Fronteira Sul.
- Just an example of socket communication.  
- The server receives a file with products, quantity and values to calculate and return the sum of them.

### Running
First, we should create one file with products details. 
* *list_of_products* is a list of some products found at internet. 
* *file_destination* is the target file for we use after.

```sh
$ python create_products.py number_of_products list_of_products file_destination
```
```sh
$ python server.py 
```
```sh
$ python client.py file_products
```

### Example
```sh
$ python create_products.py 10 products.txt file3.txt
```
```sh
$ python server.py
```
```sh
$ python client file3.txt
```

*NatanJMai*
