![Holberton school logo](https://secure.meetupstatic.com/photos/event/b/c/5/6/highres_475548214.jpeg)
# `AirBnB Clone - The Console`

## Table of Contents
* [Description](#description)
* [Installation](#installation)
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

## `Usage`
```
juanzuluaga@MacBook-de-Juan ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```

## `Bugs`
No known bugs. Please contact any of the authors if a bug appears.


## `Authors`
* **Juan Pablo Zuluaga** - [juanzuluaga91](https://github.com/juanzuluaga91) - [@juanzuluaga91](https://twitter.com/juanzuluaga91)

* **Julian Naranjo** - [JDorangetree](https://github.com/JDorangetree)) - [@JD_orangetree](https://twitter.com/JD_orangetree)