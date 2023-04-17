s = '07:05:45PM'
r = ''

times = {'01': '13', '02': '14', '03': '15', '04': '16', '05': '17', '06': '18', '07': '19', '08': '20', '09': '21',
         '10': '22', '11': '23', '12': '00'}
if 'PM' in s:
    if '12' in s:
        r = s.replace('PM', '')
        print(r)
    else:
        r = s.replace(s[0:2], times[s[0:2]])
        r = r.replace('PM', '')
        print(r)

else:
    if '12' in s:
        r = s.replace(s[0:2], times[s[0:2]])
        r = r.replace('AM', '')
        print(r)
    else:
        r = s.replace('AM', '')

