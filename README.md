# Student Guesser using Decision Tree Classifier
Hello!
This project is a self work for our Machine Learning course during our 6th semester. Contributors to the project are me (Rohan Srinivasan) and my classmate and good friend Peddi Giridhar (ID: Giridhar4).

### Pre-Requisite
```
pip install -U scikit-learn
```
### Dataset Location
/dataset/6ECEINATOR.csv

# Working of Model
The classifier works on the basis of a custom dataset made for the students of our class.
We split them into various categories of differences and make a csv file out of that.
Parameters used to split/categorise them are:
* Gender
* Part of India they belong to (East, West, North or South)
* Height (Kept Mustafa's height as reference for taller or shorter)
* Glasses
* Bencher (Sits at the front, middle, or back banches)
* Personality (Introverted, Extroverted or No Idea)
* Participation (How much do they participate in class activities)
* Licence (Drivers licence)
* Age (More than 21 or not)

The paramters are then encoded to labels.

Finally the dataset is trained on a decision tree classifier.

### Model Accuracy: 86.5%