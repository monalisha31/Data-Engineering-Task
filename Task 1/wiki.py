import wikipedia
import json
import os
results = []
def query(key, num_url, output):
  topics=wikipedia.search(key, results = num_url, suggestion = False)
  for topic in topics:
    topic_str=str(topic)
    para= wikipedia.summary(topic_str, sentences=2)
    page = wikipedia.page(topic_str)
    
    url=page.url
    wiki_dict = {}
    wiki_dict['url'] = url
    wiki_dict['paragraph'] = para
    results.append(wiki_dict)
  
  
  with open(output+'.json', 'w', encoding='utf-8') as f:
    json.dump(results , f, ensure_ascii=False,sort_keys=True, indent=4)
