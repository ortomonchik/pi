book(Da Vinci Code, Crime & Thriller & Adventure, 1, 400).
book(Harry Potter, Childrens Fiction, 7, 669).
book(Angels and Demons, Crime & Thriller & Adventure, 1, 300).
book(Lord of the Rings, Childrens Fiction, 3, 800).
book(Hannibal, Crime & Thriller & Adventure, 1, 700).

little(X):- book(X, _, _, Y), Y < 500. 		
for_children(X):- book(X, Childrens Fiction, _, _). 		
cost(X, Y):- book(X, _, _, y).
