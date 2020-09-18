# DeepLearning-DNSoverHTTPS  
## Purpose: Exploring use of machine learning and deep learning techniques on the [CIRA-CIC-DoHBrw-2020 dataset](https://www.unb.ca/cic/datasets/dohbrw-2020.html).  

### Dataset Download  
In order to download the dataset to your local machine (~2.6GB), execute the `dl-data.sh` script in your linux terminal or visit the CIRA-CIC-DoHBrw-2020 link above. If the links in the script are broken, please create an issue to notify us.  

Once the dataset is downloaded, it should look something like this:  
```
$ du doh_dataset/ -h
255M	doh_dataset/BenignDoH-NonDoH-CSVs/CSVs/Chrome/Separate
508M	doh_dataset/BenignDoH-NonDoH-CSVs/CSVs/Chrome
206M	doh_dataset/BenignDoH-NonDoH-CSVs/CSVs/Firefox/Separate
412M	doh_dataset/BenignDoH-NonDoH-CSVs/CSVs/Firefox
920M	doh_dataset/BenignDoH-NonDoH-CSVs/CSVs
920M	doh_dataset/BenignDoH-NonDoH-CSVs
98M	doh_dataset/MaliciousDoH-CSVs/CSVs/dns2tcp
0	doh_dataset/MaliciousDoH-CSVs/CSVs/dnscat2/Separate
22M	doh_dataset/MaliciousDoH-CSVs/CSVs/dnscat2
28M	doh_dataset/MaliciousDoH-CSVs/CSVs/iodine
147M	doh_dataset/MaliciousDoH-CSVs/CSVs
147M	doh_dataset/MaliciousDoH-CSVs
766M	doh_dataset/Total-CSVs
2.6G	doh_dataset/
```

### To Do:
- [ ] Documentation
  - Are there sufficient comments on functions
  - [ ] Presentation-worthy Notebooks
    - Are jupyter notebooks presentable? How much would I have to do to prepare them for a presentation? (Ideally, none!)
  - [ ] Downloading dataset
  - [ ] Discussion of dataset
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
    - [ ] [GradientBoost (GB)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html)

### Additional Reading and Resources for DNS over HTTPS
 - [SANS](https://www.sans.org/reading-room/whitepapers/dns/paper/39160)
 - [NCC](https://research.nccgroup.com/2020/03/30/impact-of-dns-over-https-doh-on-dns-rebinding-attacks/)
 - [DoH Insight: Detecting DNS over HTTPS by Machine Learning](https://dl.acm.org/doi/10.1145/3407023.3409192)
 - [Detecting Malicious DNS over HTTPS Traffic in Domain Name System using Machine Learning Classifiers](http://pubs.sciepub.com/jcsa/8/2/2/index.html)
 
