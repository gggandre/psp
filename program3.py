# ----------------------------------------------------------
# Program 3 PSP
#
# Date: 12-Mar-2022
# Authors:
#           A01753176 Gilberto André García Gaytán
# ----------------------------------------------------------
import math


# The Node class is a blueprint for creating objects that have two attributes: x and y. 
# 
# The Node class also has a method called __init__, which is a special method that is called when a
# Node object is created. 
# 
# The __init__ method has two parameters: self and data. The self parameter is a reference to the
# current instance of the class, and is used to access variables that belong to the class. 
# 
# The data parameter is the data that will be stored in the node. 
# 
# The __init__ method sets the data of the node to the value stored in the data parameter and
# initializes the next attribute to None
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None


# The class LinkedList is a class that contains a head node, a count of the number of nodes in the
# list, and the sums of the x, y, xy, x^2, and y^2 values of the nodes in the list.
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        self.sum_x = 0
        self.sum_y = 0
        self.sum_xy = 0
        self.sum_x2 = 0
        self.sum_y2 = 0

    def insert(self, x, y):
        """
        It inserts a new node at the beginning of the list.
        :param x: the x-coordinate of the point
        :param y: the dependent variable
        """
        nuevo = Node(x, y)
        nuevo.next = self.head
        self.head = nuevo
        self.count += 1
        self.sum_x += x
        self.sum_y += y
        self.sum_xy += x * y
        self.sum_x2 += x ** 2
        self.sum_y2 += y ** 2

    """
    > The function calculates the regression coefficients and the correlation coefficient for a linear
    regression model
    :return: beta0, beta1, r_xy, r2
    """
    def calular_regresion(self):
        if self.count == 0:
            return 0, 0, 0, 0
        else:
            beta1 = (self.count * self.sum_xy - self.sum_x * self.sum_y) / \
                    (self.count * self.sum_x2 - self.sum_x ** 2)
            beta0 = (self.sum_y - beta1 * self.sum_x) / self.count
            r_xy = (self.count * self.sum_xy - self.sum_x * self.sum_y) / \
                   math.sqrt((self.count * self.sum_x2 - self.sum_x ** 2) *
                             (self.count * self.sum_y2 - self.sum_y ** 2))
            r2 = r_xy ** 2
            return beta0, beta1, r_xy, r2

    def predict(self, x_k):
        """
        > The function `predict` takes a single argument `x_k` and returns the predicted value of `y_k`
        based on the regression line
        :param x_k: The value of x that we want to predict the value of y for
        :return: The predicted value of y for a given x.
        """
        beta0, beta1, _, _ = self.calular_regresion()
        y_k = beta0 + beta1 * x_k
        return y_k


print("Este programa calcula la regresión lineal y la predicción mejorada para un conjunto de n pares de datos")
numeros = int(float(input("Ingresa el número de pares de datos a calcular: ")))
linked_list = LinkedList()

for i in range(numeros):
    x = float(input("Ingresa el valor x del par {}: ".format(i+1)))
    y = float(input("Ingresa el valor y del par {}: ".format(i+1)))
    linked_list.insert(x, y)

beta0, beta1, r_xy, r2 = linked_list.calular_regresion()
print("beta0: {}".format(beta0))
print("beta1: {}".format(beta1))
print("r_xy: {}".format(r_xy))
print("r2: {}".format(r2))

x_k = float(input("Ingresa el valor de x_k para predecir su correspondiente y_k: "))
y_k = linked_list.predict(x_k)
print("y_k: {}".format(y_k))
