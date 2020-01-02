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
$$tf_{i,j} =\frac{n_{i,j}}{\sum{n_{k,j}}}$$

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

- the comparsion of prep.
- Article richness
- word cloud
- naive model
- vsm model
- average sentence length
- usage of mark
- average word length

