# DeepLearning-DNSoverHTTPS  
## Purpose: Exploring use of machine learning and deep learning techniques on the [CIRA-CIC-DoHBrw-2020 dataset](https://www.unb.ca/cic/datasets/dohbrw-2020.html).  

=======
### Feature Selection
Using the `chi2` function from `sklearn`, we conducted feature analysis on the CIRA-CIC-DoHBrw-2020 dataset. We have sorted the p-values acquired for both layers of the dataset and presented them in tables below:  

**Table 1: p-Values for Layer 1**  
| Rank | Feature | p-value |
| ---- | ------- | ------- |
| 0 | Duration | 0.0 |
| 1 | ResponseTimeTimeSkewFromMedian | 0.0 |
| 2 | ResponseTimeTimeMode | 0.0 |
| 3 | ResponseTimeTimeMedian | 0.0 |
| 4 | ResponseTimeTimeMean | 0.0 |
| 5 | PacketTimeSkewFromMedian | 0.0 |
| 6 | PacketTimeMode | 0.0 |
| 7 | PacketTimeMedian | 0.0 |
| 8 | PacketTimeMean | 0.0 |
| 9 | ResponseTimeTimeSkewFromMode | 0.0 |
| 10 | PacketTimeVariance | 0.0 |
| 11 | PacketLengthCoefficientofVariation | 0.0 |
| 12 | PacketTimeStandardDeviation | 0.0 |
| 13 | PacketLengthMode | 0.0 |
| 14 | PacketLengthMedian | 0.0 |
| 15 | PacketLengthMean | 0.0 |
| 16 | FlowBytesSent | 0.0 |
| 17 | ResponseTimeTimeCoefficientofVariation | 0.0 |
| 18 | PacketLengthStandardDeviation | 2.4524056774817733e-133 |
| 19 | PacketLengthVariance | 2.8420103297092304e-130 |
| 20 | PacketTimeCoefficientofVariation | 2.2446574541073784e-48 |
| 21 | FlowReceivedRate | 3.0280184176306084e-41 |
| 22 | ResponseTimeTimeStandardDeviation | 1.8953261120299275e-36 |
| 23 | PacketLengthSkewFromMode | 1.3596111074284224e-11 |
| 24 | FlowBytesReceived | 2.8045464210177e-09 |
| 25 | PacketLengthSkewFromMedian | 0.0018684780783491894 |
| 26 | FlowSentRate | 0.5050782607263952 |
| 27 | ResponseTimeTimeVariance | 0.552312640395313 |
| 28 | PacketTimeSkewFromMode | 0.6423484584453513 |

**Table 2: p-Values for Layer 2**
| Rank | Feature | p-value |
| ---- | ------- | ------- |
| 0 | PacketLengthStandardDeviation | 0.0 |
| 1 | PacketLengthCoefficientofVariation | 0.0 |
| 2 | FlowReceivedRate | 1.4509393684330502e-244 |
| 3 | PacketLengthMean | 7.975795053604478e-217 |
| 4 | Duration | 2.5100286975687018e-216 |
| 5 | PacketTimeSkewFromMedian | 4.5619016098941166e-188 |
| 6 | FlowSentRate | 1.859600837373798e-176 |
| 7 | PacketLengthVariance | 5.351374777063517e-147 |
| 8 | PacketTimeMean | 1.8573411824222946e-131 |
| 9 | PacketTimeStandardDeviation | 3.619943841464277e-129 |
| 10 | ResponseTimeTimeMedian | 3.3644452151914295e-115 |
| 11 | PacketTimeMedian | 5.1473782869866574e-95 |
| 12 | ResponseTimeTimeSkewFromMode | 9.87271914732135e-91 |
| 13 | ResponseTimeTimeMean | 1.5892326599083419e-62 |
| 14 | ResponseTimeTimeMode | 4.342812384163371e-61 |
| 15 | PacketTimeCoefficientofVariation | 6.0874657960560134e-59 |
| 16 | ResponseTimeTimeSkewFromMedian | 1.3816825430835129e-49 |
| 17 | PacketTimeMode | 8.24339473458698e-34 |
| 18 | FlowBytesSent | 3.9895473397653085e-29 |
| 19 | FlowBytesReceived | 4.973309049879802e-28 |
| 20 | PacketLengthMode | 3.108598107822633e-26 |
| 21 | ResponseTimeTimeCoefficientofVariation | 1.8364818379810112e-14 |
| 22 | PacketLengthSkewFromMedian | 8.143817189216589e-11 |
| 23 | PacketTimeVariance | 8.364485150112067e-06 |
| 24 | PacketLengthMedian | 5.997377954545353e-05 |
| 25 | PacketTimeSkewFromMode | 6.506025669785965e-05 |
| 26 | ResponseTimeTimeStandardDeviation | 0.01694300833098551 |
| 27 | ResponseTimeTimeVariance | 0.034534840500805755 |
| 28 | PacketLengthSkewFromMode | 0.9945070405378466 |

We can see that in Layer 1, there are a lot of zeros! This would mean there are a lot of features that either directly correlate to the target classification *or* (what I believe is more likely), the p-values are too small for Python (< 1e-308).

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
- [x] Feature Selection
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
 
