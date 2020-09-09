# Remove all \n and url link in answer
_data = re.sub(r"(\\n)|(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)", '.', str(raw[count-1+i]))