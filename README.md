# Reuters-full-data-set
Full unofficial data set of Reuters composed of 8,551,441 news titles, links and timestamps (Jan 2007 - Aug 2016).

```
git clone https://github.com/philipperemy/Reuters-full-data-set.git
python read.py
```

```
ts = 20070228 11:46 AM EST, t = European stocks hit 7-week low amid new sell-off, h= http://www.reuters.com/article/companyNewsAndPR/idUSWEB277620070228
ts = 20070228 11:46 AM EST, t = Schering-Plough announces Ismail Kola as VP and Chief Scientific Officer, h= http://www.reuters.com/article/inPlayBriefing/idUSIN20070228164651SGP20070228
ts = 20070228 11:46 AM EST, t = O'Reilly Automotive forecasts 2007 earnings growth, h= http://www.reuters.com/article/marketsNews/idUSN2845320220070228
ts = 20070228 11:42 AM EST, t = Market Wrap, h= http://www.reuters.com/article/inPlayBriefing/idUSIN20070228164235WRAPX20070228
ts = 20070228 11:42 AM EST, t = Chile's CMPC net profit falls 13 pct in 2006, h= http://www.reuters.com/article/tnBasicIndustries-SP/idUSN2844077020070228
ts = 20070228 11:42 AM EST, t = Toyota Venezuela to halt March ops on currency woes, h= http://www.reuters.com/article/tnBasicIndustries-SP/idUSN2827887820070228
```

Each pickle file in `data` represents a day (e.g. `20160102.pkl` is for Jan, 2 2016).

One day is composed of several news, gathered in a `list`.

Each news is a `dict` of the form:

```
ts: timestamp of the form 20070228 11:46 AM EST
title: title of the news
href: link to the article to get the full content
```
