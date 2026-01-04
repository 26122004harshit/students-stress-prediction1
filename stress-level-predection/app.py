import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')  # Specify the directory for templates

# Load dataset

         

