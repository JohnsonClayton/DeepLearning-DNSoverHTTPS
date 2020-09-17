# DeepLearning-DNSoverHTTPS  
## Purpose: Exploring use of machine learning and deep learning techniques on the [CIRA-CIC-DoHBrw-2020 dataset](https://www.unb.ca/cic/datasets/dohbrw-2020.html).  

### To Do:
- [ ] Literature Survey/Related Works
  - What is the problem and why are we interested in it?  
  - What previous work has been done applying ML and DL?
  - What gap in the research exists so that our contribution could be as significant and helpful as possible?
- [ ] Dataset Description
  - Describe the dataset and how its features are generated
  - What do the features describe and how are they useful?
  - Could bias be introduced into the dataset through the collection techniques used?
- [ ] Feature Selection
  - Use [chi-squared](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html) or other techniques
    - [This](https://towardsdatascience.com/chi-square-test-for-feature-selection-in-machine-learning-206b1f0b8223) may be helpful
  - What features are needed for the models to perform adequately on the problems at hand?
- [ ] Feature Analysis
  - What about the selected features make them useful from a predictive capability point of view?
  - Distribution plots as seen at the end of [this](https://github.com/rambasnet/DeepLearningMaliciousURLs/blob/master/feature%20analysis.ipynb) jupyter notebook
- [ ] Experiments  
  - [ ] DNN Models
    - [ ] [Keras-TensorFlow](https://keras.io/)
    - [ ] [Fast.ai (v2)](https://docs.fast.ai/quick_start.html)
  - [ ] Traditional ML Models
    - [ ] [Decision Tree (DT)](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
    - [ ] [Logistic Regression (LR)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
    - [ ] [Linear Discriminant Analysis (LDA)](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html)
    - [ ] [k-Nearest Neighbors (kNN)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
    - [ ] [Naive Bayes (NB)](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)
    - [ ] [Support Vector Machines (SVM)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
  - [ ] Ensemble Methods
    - [ ] [Random Forest (RF)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
    - [ ] [AdaBoost (AB)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html)

### Additional Reading and Resources for DNS over HTTPS
 - [SANS](https://www.sans.org/reading-room/whitepapers/dns/paper/39160)
 - [NCC](https://research.nccgroup.com/2020/03/30/impact-of-dns-over-https-doh-on-dns-rebinding-attacks/)
 
