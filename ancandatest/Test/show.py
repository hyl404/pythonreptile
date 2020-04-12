import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from  pyecharts.faker import Faker
df = pd.read_csv('1.csv')

data = [['北京',331],['西藏',18],['湖北',103],['上海',298],['天津',350],['陕西',51],['安徽',106]]
c = (
    Map()
    .add("上市公司数量",data,"china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="上市公司数量分布图"),
        visualmap_opts=opts.VisualMapOpts(max_=700)
    )
)
c.render()