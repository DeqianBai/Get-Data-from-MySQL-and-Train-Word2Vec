# Get-Data-from-MySQL-and-Train-Word2Vec

## 获取数据

用到两份数据：

1. 新闻语料库
    
       新闻语料存放在云数据库，配置为 Mysql; 通过 DataGrip 进行数据库访问
       
2. WiKi中文语料库
    
       下载地址：https://dumps.wikimedia.org/zhwiki/20190720/

## 训练Word2Vec

分两步：

先使用WiKi中文语料库训练

再使用新闻语料库继续训练
