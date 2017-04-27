import re
search='alt="checked'
text='<li style="padding-right: 12px"><img alt="not checked" height="14" src="/includes/images/common/ico_chkbox_on.gif" width="16"/>Master\'s</li>'
result = re.findall('\\b'+search+'\\b', text, flags=re.IGNORECASE)
print(result)