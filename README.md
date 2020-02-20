![Holberton school logo](https://secure.meetupstatic.com/photos/event/b/c/5/6/highres_475548214.jpeg)
# `AirBnB Clone - The Console`

## Table of Contents
* [Description](#description)
* [Installation](#installation)
* [File Description](#File-Description)
* [Usage](#usage)
* [Bugs](#bugs)
* [Authors](#authors)


## `Description`
A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and   “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.


## `Installation`

Clone this repository: git clone "https://github.com/JDorangetree/AirBnB_clone.git"
Access AirBnb directory: cd AirBnB_clone
Run hbnb(interactively): ./console and enter command
Run hbnb(non-interactively): echo "<command>" | ./console.py

## `File Description`


### `console.py`

List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

### `base_model.py - The BaseModel class from which future classes will be derived`

* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

### `Classes inherited from Base Model:`

* amenity.py
* city.py
* place.py
* review.py
* state.py
* user.py

#### `File Storage class that handles JASON serialization and deserialization :`

file_storage.py- serializes instances to a JSON file & deserializes back to instances

* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* `def reload(self)` -  deserializes the JSON file to __objects









## `Usage`
```
juanzuluaga@MacBook-de-Juan ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

hbnb) create BaseModel
fea31bb8-ac52-4a33-a9fe-e02e08177891
(hbnb) all BaseModel
[[BaseModel] (798c4604-06c1-4d85-904c-0802403946c1) {'id': '798c4604-06c1-4d85-904c-0802403946c1', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 19, 775151), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 19, 775241)}, [BaseModel] (2cdde9c6-d49e-4a44-a347-da1e654a161d) {'id': '2cdde9c6-d49e-4a44-a347-da1e654a161d', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 22, 858442), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 22, 858510)}, [BaseModel] (fea31bb8-ac52-4a33-a9fe-e02e08177891) {'id': 'fea31bb8-ac52-4a33-a9fe-e02e08177891', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 27, 3197), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 27, 3260)}]
(hbnb) all
[[User] (e2d9493c-e10c-4a05-91ad-8c4650af6f1c) {'id': 'e2d9493c-e10c-4a05-91ad-8c4650af6f1c', 'created_at': datetime.datetime(2020, 2, 18, 21, 0, 40, 83444), 'updated_at': datetime.datetime(2020, 2, 18, 21, 0, 40, 83492)}, [BaseModel] (798c4604-06c1-4d85-904c-0802403946c1) {'id': '798c4604-06c1-4d85-904c-0802403946c1', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 19, 775151), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 19, 775241)}, [BaseModel] (2cdde9c6-d49e-4a44-a347-da1e654a161d) {'id': '2cdde9c6-d49e-4a44-a347-da1e654a161d', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 22, 858442), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 22, 858510)}, [BaseModel] (fea31bb8-ac52-4a33-a9fe-e02e08177891) {'id': 'fea31bb8-ac52-4a33-a9fe-e02e08177891', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 27, 3197), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 27, 3260)}]
(hbnb) create User
bd2d397c-6464-4434-94d2-4afc587632de
(hbnb) all
[[User] (e2d9493c-e10c-4a05-91ad-8c4650af6f1c) {'id': 'e2d9493c-e10c-4a05-91ad-8c4650af6f1c', 'created_at': datetime.datetime(2020, 2, 18, 21, 0, 40, 83444), 'updated_at': datetime.datetime(2020, 2, 18, 21, 0, 40, 83492)}, [BaseModel] (798c4604-06c1-4d85-904c-0802403946c1) {'id': '798c4604-06c1-4d85-904c-0802403946c1', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 19, 775151), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 19, 775241)}, [BaseModel] (2cdde9c6-d49e-4a44-a347-da1e654a161d) {'id': '2cdde9c6-d49e-4a44-a347-da1e654a161d', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 22, 858442), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 22, 858510)}, [BaseModel] (fea31bb8-ac52-4a33-a9fe-e02e08177891) {'id': 'fea31bb8-ac52-4a33-a9fe-e02e08177891', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 27, 3197), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 27, 3260)}, [User] (bd2d397c-6464-4434-94d2-4afc587632de) {'id': 'bd2d397c-6464-4434-94d2-4afc587632de', 'created_at': datetime.datetime(2020, 2, 19, 10, 0, 37, 668147), 'updated_at': datetime.datetime(2020, 2, 19, 10, 0, 37, 668206)}]
(hbnb) all BaseModel
[[BaseModel] (798c4604-06c1-4d85-904c-0802403946c1) {'id': '798c4604-06c1-4d85-904c-0802403946c1', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 19, 775151), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 19, 775241)}, [BaseModel] (2cdde9c6-d49e-4a44-a347-da1e654a161d) {'id': '2cdde9c6-d49e-4a44-a347-da1e654a161d', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 22, 858442), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 22, 858510)}, [BaseModel] (fea31bb8-ac52-4a33-a9fe-e02e08177891) {'id': 'fea31bb8-ac52-4a33-a9fe-e02e08177891', 'created_at': datetime.datetime(2020, 2, 19, 9, 57, 27, 3197), 'updated_at': datetime.datetime(2020, 2, 19, 9, 57, 27, 3260)}]
(hbnb) all User
[[User] (e2d9493c-e10c-4a05-91ad-8c4650af6f1c) {'id': 'e2d9493c-e10c-4a05-91ad-8c4650af6f1c', 'created_at': datetime.datetime(2020, 2, 18, 21, 0, 40, 83444), 'updated_at': datetime.datetime(2020, 2, 18, 21, 0, 40, 83492)}, [User] (bd2d397c-6464-4434-94d2-4afc587632de) {'id': 'bd2d397c-6464-4434-94d2-4afc587632de', 'created_at': datetime.datetime(2020, 2, 19, 10, 0, 37, 668147), 'updated_at': datetime.datetime(2020, 2, 19, 10, 0, 37, 668206)}]
```

## `Bugs`
No known bugs. Please contact any of the authors if a bug appears.


## `Authors`
* **Juan Pablo Zuluaga** - [juanzuluaga91](https://github.com/juanzuluaga91) - [@juanzuluaga91](https://twitter.com/juanzuluaga91)

* **Julian Naranjo** - [JDorangetree](https://github.com/JDorangetree) - [@JD_orangetree](https://twitter.com/JD_orangetree)
