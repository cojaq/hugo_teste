---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Exemplo de jupyter notebook"
subtitle: ""
summary: "teste com jupyter notebook"
authors: 
 - tiago
tags: []
categories: []
date: 2019-09-09T01:07:42-03:00
lastmod: 2019-09-09T01:07:42-03:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  placement: 2
  caption: "Credit"
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

# Question 4

Apply a smooth-method in the weather time-series, using question 1. Plot the content using any plot package.


```python
#a funcao faz tres graficos, simulando uma aproximacao/zoom para facilitar a visualizacao do efeito da media movel
def plot_smooth(serie, cut1="", cut2="", yt="", title=""):
    
    if not cut1:
        cut1 = serie.index.year[int(len(serie) - (len(serie)/4))]
    if not cut2:
        cut2 = serie.index.year[int(len(serie) - ((len(serie)/4)/4))]
    
    fig, axes = plt.subplots(3, 1, figsize=(16, 9))
    series = [serie, serie[str(cut1) : str(serie.index.year[-1])], serie[str(cut2) : str(serie.index.year[-1])]]
    
    for s, ax in zip(series,axes):

        serie_daily = s
        #media movel de 7, 30 e 365 dias                        
        serie_7d = serie_daily.rolling(7, center=True).mean()
        serie_30d = serie_daily.rolling(30, center=True).mean()
        serie_365d = serie_daily.rolling(365, center=True).mean()
       
        ax.plot(serie_daily, marker='.', markersize=2, color='0.6',lw=0.6, label='Diário')
        ax.plot(serie_7d, linewidth=1.4, label='Média móvel 7 dias')
        ax.plot(serie_30d, linewidth=2.2, label='Média móvel 30 dias')
        ax.plot(serie_365d, color='0.2', linewidth=3, label='Média móvel 365 dias')
        
        ax.legend()
        ax.set_ylabel(yt)
    
    axes[0].axvspan(str(cut1), str(serie.index.date[-1]), color=sns.xkcd_rgb['yellow'], alpha=0.3)
    axes[1].axvspan(str(cut2), str(serie.index.date[-1]), color=sns.xkcd_rgb['yellow'], alpha=0.3)
    
    fig.suptitle(title)
    return

plot_smooth(temp1, yt='Temperatura (C)', title='Tendências da temperatura (Estação 59999)')
plot_smooth(temp2, yt='Temperatura (C)', title='Tendências da temperatura (Estação 60020)')
plot_smooth(temp3, yt='Temperatura (C)', title='Tendências da temperatura (Estação 60046)')
```


![png](./questions_python_RESOLVIDAS_TIAGO_32_0.png)



![png](./questions_python_RESOLVIDAS_TIAGO_32_1.png)



![png](./questions_python_RESOLVIDAS_TIAGO_32_2.png)



```python

```

<hr>
