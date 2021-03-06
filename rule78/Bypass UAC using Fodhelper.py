from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "event_id": "13"
          }
        },
        {
          "wildcard": {
            "registry_key_path.keyword":"*\\\\ms-settings\\\\shell\\\\open\\\\command\\\\*"
          }
        }
      ]
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Privilege Escalation"
technique = "Bypass User Account Control"
procedure = "Bypass UAC using Fodhelper"
tech_code = "T1088"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 53)

print('Bypass UAC using Fodhelper.py '+ str(count))