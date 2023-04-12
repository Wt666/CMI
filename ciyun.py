from wordcloud import WordCloud
wc = WordCloud()    # 创建词云对象
wc.generate('weixin gongzhonghao CoderAdai yangmingblog.cn')    # 生成词云
wc.to_file('cy.png')    # 保存词云
