import re
f = open('output_log')
data = f.readlines()
f.close()
header =f'''{{
  "name": "Log",
  "examples": ['''
f =open('log.json','w')
f.write(header)
f.write('\n')
for ix in range(len(data)):
    try:
        start_idx = data[ix].index('START')
        stop_idx = data[ix].index('STOP')
        if start_idx and stop_idx:
            resp=f'''{{
            "string": "{user_string}",
            "match": [
            {{
            "start":{start_id},
            "end":{stop_idx}
            }}
                    ]
                    }},'''
            f.write(resp)
            f.write('\n')
    except:
        pass
f.write(']')
f.write('\n')
f.write('}')
f.close()
