# 七猫小说网男生小说数据分析
    
## 项目概览

**目标网站**：七猫中文网男生小说专区  
**数据规模**：男生小说共7718本  
**技术**：Scrapy爬取 × 多维度分析 × 数据可视化

## 分析目标

| 维度   | 分析指标         | 可视化方案         |
|------|--------------|---------------|
| 基础分布 | 字数区间占比、类型占比  | 环形图+饼图        |
| 对比分析 | 类型平均字数条形图    | 横向对比柱状图       |
| 质量评估 | 评分正态分布曲线     | 散点图+高斯分布      |
| 标签生态 | 高频标签组合       | 动态词云图         |
| 关联分析 | 字数-评分相关性     | 动态散点图         |
| 榜单经济 | 双榜Top20作品    | 水球图+左右横向对比柱状图 |
| 类型榜单 | 双榜各类型Top20作品 | 自动横向轮播柱状图     |
| 作者价值 | Top20高产作者    | 立体柱状图         |

### 爬虫

```mermaid
graph TD
    A[Scrapy框架] --> B[Xpath页面解析]
    B --> C[简单数据处理]
    C --> D[MongoDB集群]
``` 

### 技术
**爬虫引擎**  
[![Scrapy](https://img.shields.io/badge/Scrapy-2.12+-green)](https://scrapy.org)  
**数据存储**  
[![MongoDB](https://img.shields.io/badge/MongoDB-4.10+-blue)](https://mongodb.p2hp.com/)  
**分析引擎**  
[![Pandas](https://img.shields.io/badge/Pandas-2.2+-red)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.1+-orange)](https://numpy.org/)
[![Scipy](https://img.shields.io/badge/Scipy-1.14+-yellow)](https://docs.scipy.org/)  
**可视化**  
[![Pyecharts](https://img.shields.io/badge/Pyecharts-2.0+-purple)](https://pyecharts.org/)  

### 日志
| 阶段   | 关键技术       | 耗时  | 突破点       |
|------|------------|-----|-----------|
| 爬虫开发 | XPath动态解析  | 10h | 网页数据不一致   |
| 数据清洗 + 可视化  | Pandas提取清洗、画面整体处理 | 13h | 动态交互实现    |

### 总榜单

---

总累计人气TOP3
1. 《一剑独尊》- 10058.2万
2. 《我有一剑》- 7377.8万
3. 《太荒吞天诀》- 5659.7万

阅读量TOP3
1. 《太荒吞天诀》- 322.4万
2. 《剑来》- 203万
3. 《无敌天命》- 196.5万

![七猫人气and阅读Top20](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫人气and阅读Top20.png)
[七猫人气and阅读Top20](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫人气and阅读Top20.html)

- 总人气值和总阅读量的Top20作品有40%的重合。
- 不难发现人气榜全为老书，而阅读榜中有60%为新书。
- 老书依旧韵味十足，新书也迸发着强劲活力，这正是一个新老逐渐交替的时候。

![最多产作者排行榜](https://themilkyway01.github.io/qimao-novels-analysis/images/最多产作者排行榜.png)
[最多产作者排行榜](https://themilkyway01.github.io/qimao-novels-analysis/images/最多产作者排行榜.html)

- 又从作者产出来看，产出最多的都是老作者，说明急需新作者的进入和沉淀。

### 用户需求分析

---

![七猫各类型在线阅读榜](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫各类型在线阅读榜.png)
[七猫各类型在线阅读榜](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫各类型在线阅读榜.html)

![七猫各类型累计人气榜](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫各类型累计人气榜.png)
[七猫各类型累计人气榜](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫各类型累计人气榜.html)

| 类别   | 表现特征      | 用户需求解读   |
|------|-----------|----------|
| 都市类  | 双榜数据领跑 | 带入自身为角色 |
| 现实题材 | 数据持续低位 | 现实而不想接受 |

### 字数区间

---

![七猫男生原创小说字数分布](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫男生原创小说字数分布.png)
[七猫男生原创小说字数分布](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫男生原创小说字数分布.html)

```mermaid
graph LR
  A[字数分析] --> B{小于50万}
  A --> C[50-200万]
  A --> D{大于200万}
  B --> E(烂尾风险高)
  C --> F(创作黄金区间)
  D --> G(需IP开发赋能)
  G --> H(其他相关)
  H --> I(短视频)
  H --> J(漫画)
  H --> K(动漫)
  H --> L(...)
```

### 字数与评分的相关性

---

![七猫字数与评分的相关性](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫字数与评分的相关性.png)
[七猫字数与评分的相关性](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫字数与评分的相关性.html)

- 字数越多，评分并不一定越高，但字数越低评分可能会越低。
- 两者并没有强相关性

### 高频标签组合

---

**标签组合TOP3:**  
**TOP1**：东方玄幻
**TOP2**：都市高武
**TOP3**：都市高手

**运营建议:**  
1. 建立新书孵化计划：针对<50万作品设置创作激励  
2. IP联动开发池：筛选200万+优质长篇进行漫改/影视化  
3. 设立「新类型探索奖」：都市+玄幻跨界创作（大胆推测）  

![七猫高频标签组合](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫高频标签组合.png)
[七猫高频标签组合](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫高频标签组合.html)

### 特殊发现

---

![七猫评分分布曲线](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫评分分布曲线.png)
[七猫评分分布曲线](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫评分分布曲线.html)

- 评分呈现`右偏分布`，主要集中在`8.0~9.0`之间 ➥ 疑似新书默认8.0分机制影响（猜测）

### 其他

---

![七猫各类型平均字数对比](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫各类型平均字数对比.png)
[七猫各类型平均字数对比](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫各类型平均字数对比.html)

![七猫男生原创小说类型分布](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫男生原创小说类型分布.png)
[七猫男生原创小说类型分布](https://themilkyway01.github.io/qimao-novels-analysis/images/七猫男生原创小说类型分布.html)
