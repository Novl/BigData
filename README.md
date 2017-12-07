## Hadoop practice task

commands.sh -- assumed executing steps

_folders_:    
/bigdata1 -- with datafile __star2002-full.csv__  
/bigdata2 -- with quantile's  
/bigdata3 -- with **antiNucleus** and counts distinct **eventFile**  
/bigdata4 -- with **antiNucleus** and mean **Pt**   


_workers_:
* work1: map1.py , reduce1.py -- finds the quantile's 0.05 and 0.95 of **prodTime** and store as result in /bigdata2  

* work2: map2.py , reduce2.py -- counts distinct **eventFile** for each **antiNucleus** that have **prodTime** in quantiles  

* work3: map3.py , reduce3.py -- mean **Pt** for each **antiNucleus** that have **prodTime** in quantiles  

Results ----------  
work1:  
    20011992.7097
    20029357.305

work2:  
    0 622826    
    1 1327878   
    10 652  
    11 242  
    12 100  
    13 40   
    14 12   
    15 2    
    16 2    
    17 1    
    2 909616    
    3 598995    
    4 304667    
    5 126244    
    6 46202  
    7 15120  
    8 5054  
    9 1647  

work3:  
    0 65.3802879277  
    1 261.818233923  
    10 49.8683280085    
    11 100.509451032    
    12 20.614649665  
    13 58.437897973  
    14 12.3384203583     
    15 29.1930735   
    16 1.41268635   
    17 0.0  
    2 311.928337864  
    3 326.398943296  
    4 333.303659974  
    5 377.776456897  
    6 238.354659937  
    7 197.92835076   
    8 205.614121095  
    9 205.173263056  