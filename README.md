# VSMgrader_DataScienceWithR
Final project of R, an English essay scorer.

### dataset:
- my essay (ranked as medium)
- sample essay from college essay exam
- https://github.com/ChiragSoni95/Autograder (use dataset only)
- http://toefl.zhan.com/
- http://irma0302.pixnet.net/
- https://www.ukessays.com/
- https://drive.google.com/drive/folders/0BxEC0dgV3WQQNHBUZzREQTZUQ3M?fbclid=IwAR2oWP_17pbs4vuKLCCzHefcNARNE4iNR2x6iDnwAuOmiITZx4ULBvhuHMc

### structure:
```
├── data
│   ├── professional
│   ├── medium
│   ├── beginner
│   ├── native 
│   └── dictionary  
├── preprocessing.py
├── vsm.py
├── vsm_v2.py
├── README.md
└── Statics (not yet)
```

### preprocessing.py
We can clean the data into csv file which record words frequency in essay and the probability of word appearance among files.
The result will save under the diretory /data/dictionary/.
The data had bulit. If new essaies are added, you will better execute the python file angin to ensure the accuary.
```
python3 preprocessing.py
```

### Model
Use vector space model to evaluate the relationship of the query and per section.

tf: the frequency of the word in an essay, which signifies the importance of the words in the essay.
idf: inverted document frequency. The larger the number is, the less impoertant does the word means.
 
### Result
The expected output maybe this for the biginner writer.
```
|======= English Level =======|
|                             |
|  beginner:     45.534302 %  |
|  medium:       13.673424 %  |
|  professional: 30.480181 %  |
|  native:       10.312093 %  |
|                             |
|=============================|

```

### Statics Data
- [ ] words in document frequency(#df)
- [ ] the comparsion of prep.
- [ ] Article richness
- [ ] word cloud
- [ ] naive model
- [ ] vsm model
- [ ] average sentence length
- [ ] usage of mark
- [ ] average word length

<h3 id="df"> words in document frequency </h3>
This section shows the statics of the a word appears in differnet essays. We discuss the word usage in 4 groups. We make a hypothesis that the lower degree english user may repeatedly use the same words among different essays due to their lacking vocabulary. **R wordcloud** is used to demostrate. 

#### Implementation

R is used to represent the word cloud. We only choose the top 35 frequency words drawing in the plot.

```r=
beginner_dat = read.csv("D:/NTU/R/VSMgrader_DataScienceWithR/data/idf_rank/beginner.csv", header = F)
head(beginner_dat)
beginner_dat <- head(beginner_dat, 35)
library(wordcloud)
wordcloud(
  words = beginner_dat$V1, 
  freq =  beginner_dat$V2, 
  scale = c(8,.10), 
  random.order = FALSE,
  ordered.colors = FALSE,
  rot.per = FALSE,
  #min.freq = 7,
  colors = brewer.pal(8,"Dark2"),
  family = "mono", 
  font = 10
)
```
Reference: https://ithelp.ithome.com.tw/articles/10192052

#### Result

- beginner: 
It is not a suprising answer to see such figure. **I** is the most popular word in beginner english. They practice writing by diary-like essay. The freqence of relative words prove the phenomenon

![](img/df_beginner.png) 
 
- medium:
The result of medium level write is intriguing. By knowing advanced grammar they always remember to put **the** before nouns, and they start to descript objectively by using **is**.

![](img/medium.png)
 
- [ ] the comparsion of prep.
- [ ] Article richness
- [ ] word cloud
- [ ] naive model
- [ ] vsm model
- [ ] average sentence length
- [ ] usage of mark
- [ ] average word length

